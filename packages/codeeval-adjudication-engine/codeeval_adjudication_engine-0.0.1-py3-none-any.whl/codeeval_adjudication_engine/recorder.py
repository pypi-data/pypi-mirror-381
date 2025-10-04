# Copyright (c) 2025-2026 Gowtham A Rao MD PhD. All Rights Reserved.
#
# This software is proprietary and dual-licensed.
# Licensed under the Prosperity Public License 3.0.0 (the "License").
# A copy of the license is available at https://prosperitylicense.com/versions/3.0.0
# For details, see the LICENSE file.
#
# Commercial use beyond a 30-day trial requires a separate license.
# Contact: rao@ohdsi.org

from datetime import datetime, timezone

from .consensus import ConsensusCalculator
from .interfaces import AuditLogger, DataAccessLayer
from .models import AdjudicationVote, AuthorizationError, VoteDecision
from .tgs_factory import TGSFactory
from .workflow_manager import WorkflowManager


class VoteRecorder:
    """
    Handles the intake of adjudication votes with strict data integrity controls,
    fulfilling FRD section AL3.
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
        Initializes the VoteRecorder with its dependencies.

        Args:
            dal: An object conforming to the DataAccessLayer interface for all
                 database operations.
            consensus_calculator: An instance of the ConsensusCalculator to apply
                                  consensus rules.
            tgs_factory: The service responsible for checking and finalizing a
                       clinical idea.
            audit_logger: The service for logging audit trails.
            workflow_manager: The service for managing the clinical idea lifecycle.
        """
        self._dal = dal
        self._consensus_calculator = consensus_calculator
        self._tgs_factory = tgs_factory
        self._audit_logger = audit_logger
        self._workflow_manager = workflow_manager

    def submit_vote(
        self,
        user_id: str,
        concept_id: int,
        decision: VoteDecision,
        clinical_idea_id: int,
    ) -> None:
        """
        Submits a vote and triggers a real-time consensus calculation within a
        single, ACID-compliant transaction.

        This method fulfills FRD requirements:
        - AL3.1: Accepts a vote.
        - AL3.2: Validates authorization and state.
        - AL3.3: Generates an authoritative, server-side timestamp.
        - AL3.5: Ensures the entire operation is transactional and uses
                 pessimistic locking.

        Args:
            user_id: The ID of the user submitting the vote.
            concept_id: The ID of the concept being voted on.
            decision: The vote decision (Include/Exclude).
            clinical_idea_id: The ID of the clinical idea being adjudicated.

        Raises:
            AuthorizationError: If the user is not an active adjudicator.
            InvalidStateError: If the clinical idea is already finalized.
            ConcurrencyConflictError: If a lock cannot be acquired on the concept.
        """
        # 1. Validation and State Management (AL1.2, AL3.2)
        # Delegate state transition and validation to the WorkflowManager.
        self._workflow_manager.start_adjudication(clinical_idea_id)

        # The WorkflowManager is also the source of truth for the roster (AL1.4).
        active_roster = self._workflow_manager.get_roster(clinical_idea_id)

        # Perform authorization check against the active roster (AL1.1).
        active_adjudicator_ids = {r.user_id for r in active_roster if r.is_active}
        if user_id not in active_adjudicator_ids:
            raise AuthorizationError(
                f"User '{user_id}' is not an active adjudicator for this clinical idea."
            )

        # 2. Auditing (NFR-AL5)
        self._audit_logger.log_vote_action(
            user_id=user_id,
            concept_id=concept_id,
            clinical_idea_id=clinical_idea_id,
            decision=decision,
        )

        # 3. Check for existing vote (AL3.4)
        existing_vote = self._dal.get_vote_by_user_and_concept(
            user_id=user_id, concept_id=concept_id
        )

        # 4. Transaction Management and Locking (AL3.5)
        with self._dal.transaction():
            # Acquire lock before any writes (AL3.5.1)
            self._dal.get_concept_status_for_update(concept_id)

            # Create the vote object with an authoritative timestamp (AL3.3)
            vote_to_persist = AdjudicationVote(
                user_id=user_id,
                concept_id=concept_id,
                decision=decision,
                timestamp=datetime.now(timezone.utc),
            )

            # Persist the vote (AL3.3, AL3.4)
            if existing_vote:
                self._dal.update_vote(vote_to_persist)
            else:
                self._dal.create_vote(vote_to_persist)

            # 5. Consensus Recalculation (AL4.1.1)
            all_votes = self._dal.get_all_votes(clinical_idea_id)
            new_consensus = self._consensus_calculator.calculate_consensus(
                concept_id=concept_id,
                all_votes=all_votes,
                active_roster=active_roster,
            )

            # 6. Update Status (AL4.4)
            self._dal.update_concept_status(concept_id, new_consensus)

            # 7. Check for Clinical Idea Finalization
            self._tgs_factory.check_and_finalize(clinical_idea_id)
