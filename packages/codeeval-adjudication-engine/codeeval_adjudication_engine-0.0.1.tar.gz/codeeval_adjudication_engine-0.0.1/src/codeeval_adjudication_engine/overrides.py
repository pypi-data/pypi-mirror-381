# Copyright (c) 2025-2026 Gowtham A Rao MD PhD. All Rights Reserved.
#
# This software is proprietary and dual-licensed.
# Licensed under the Prosperity Public License 3.0.0 (the "License").
# A copy of the license is available at https://prosperitylicense.com/versions/3.0.0
# For details, see the LICENSE file.
#
# Commercial use beyond a 30-day trial requires a separate license.
# Contact: rao@ohdsi.org

from .consensus import ConsensusCalculator
from .interfaces import AuditLogger, DataAccessLayer
from .models import (
    AuthorizationError,
    ClinicalIdeaStatus,
    InvalidStateError,
    UserContext,
)
from .tgs_factory import TGSFactory
from .workflow_manager import WorkflowManager


class OverrideManager:
    """
    Provides critical operational resilience by allowing dynamic management of the
    Adjudicator Roster, fulfilling FRD section AL7.
    """

    def __init__(
        self,
        dal: DataAccessLayer,
        consensus_calculator: ConsensusCalculator,
        tgs_factory: TGSFactory,
        audit_logger: AuditLogger,
        workflow_manager: WorkflowManager,
    ):
        """
        Initializes the OverrideManager with its dependencies.

        Args:
            dal: An object conforming to the DataAccessLayer interface.
            consensus_calculator: An instance of the ConsensusCalculator for rule
                application.
            tgs_factory: The service responsible for checking and finalizing a
                       clinical idea.
            audit_logger: The service for logging audit trails.
            workflow_manager: The service for managing the clinical idea lifecycle
                              and roster.
        """
        self._dal = dal
        self._consensus_calculator = consensus_calculator
        self._tgs_factory = tgs_factory
        self._audit_logger = audit_logger
        self._workflow_manager = workflow_manager

    def modify_adjudicator_roster(
        self,
        clinical_idea_id: int,
        user_id_to_modify: str,
        new_active_status: bool,
        current_user_context: UserContext,
    ) -> None:
        """
        Modifies an adjudicator's active status on the roster and triggers a full
        consensus recalculation for the entire clinical idea.

        This method fulfills FRD requirements:
        - AL7.1: Provides the roster modification interface.
        - AL7.2: Enforces authorization and state validation.
        - AL7.3: Triggers immediate, full consensus recalculation.
        - AL7.4: Invalidates votes of a deactivated adjudicator.
        - AL7.5: Executes all operations within a single, robust transaction.
        - AL7.6: Logs the override action to an audit trail.

        Args:
            clinical_idea_id: The ID of the clinical idea to modify.
            user_id_to_modify: The ID of the adjudicator to activate or deactivate.
            new_active_status: The new `is_active` status for the adjudicator.
            current_user_context: The context of the user performing the action.

        Raises:
            AuthorizationError: If the user is not a 'Session Lead'.
            InvalidStateError: If the clinical idea is already finalized.
            ConcurrencyConflictError: If a lock cannot be acquired during the
                transaction.
        """
        # 1. Authorization and Validation (AL7.2)
        if "Session Lead" not in current_user_context.roles:
            raise AuthorizationError("Only 'Session Lead' role can modify the roster.")

        idea_status = self._dal.get_clinical_idea_status(clinical_idea_id)
        if idea_status == ClinicalIdeaStatus.FINALIZED:
            raise InvalidStateError(
                "Cannot modify roster of a finalized clinical idea."
            )

        # 2. Auditing (AL7.6)
        action = "ACTIVATE" if new_active_status else "DEACTIVATE"
        self._audit_logger.log_override_action(
            session_lead_id=current_user_context.user_id,
            affected_adjudicator_id=user_id_to_modify,
            action=action,
            clinical_idea_id=clinical_idea_id,
        )

        # 3. Transactional Execution (AL7.5)
        with self._dal.transaction():
            # Lock all concepts for this clinical idea to prevent race conditions
            # with concurrent voting during the recalculation.
            concept_statuses = self._dal.get_all_concept_statuses_for_update(
                clinical_idea_id
            )

            # 3. Roster Update and Vote Invalidation (AL7.1, AL7.4) via WorkflowManager
            self._workflow_manager.modify_roster(
                clinical_idea_id, user_id_to_modify, new_active_status
            )

            # 4. Full Consensus Recalculation (AL7.3)
            # Fetch the fresh data needed for calculation within the transaction
            new_roster = self._workflow_manager.get_roster(clinical_idea_id)
            all_votes = self._dal.get_all_votes(clinical_idea_id)

            for concept_status in concept_statuses:
                new_consensus = self._consensus_calculator.calculate_consensus(
                    concept_id=concept_status.concept_id,
                    all_votes=all_votes,
                    active_roster=new_roster,
                )
                if new_consensus != concept_status.status:
                    self._dal.update_concept_status(
                        concept_status.concept_id, new_consensus
                    )

            # 5. Check for Clinical Idea Finalization
            self._tgs_factory.check_and_finalize(clinical_idea_id)
