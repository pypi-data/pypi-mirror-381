# Copyright (c) 2025-2026 Gowtham A Rao MD PhD. All Rights Reserved.
#
# This software is proprietary and dual-licensed.
# Licensed under the Prosperity Public License 3.0.0 (the "License").
# A copy of the license is available at https://prosperitylicense.com/versions/3.0.0
# For details, see the LICENSE file.
#
# Commercial use beyond a 30-day trial requires a separate license.
# Contact: rao@ohdsi.org

from .interfaces import AuditLogger, DataAccessLayer, TGSFinalizationNotifier
from .models import (
    ClinicalIdeaStatus,
    ConceptConsensusStatus,
    TGS_Definition,
)
from .workflow_manager import WorkflowManager


class TGSFactory:
    """
    Encapsulates the logic for finalizing a clinical idea and constructing
    the True Gold Standard (TGS), fulfilling FRD section AL5.
    """

    def __init__(
        self,
        dal: DataAccessLayer,
        notifier: TGSFinalizationNotifier,
        audit_logger: AuditLogger,
        workflow_manager: WorkflowManager,
    ):
        """
        Initializes the TGSFactory with its dependencies.

        Args:
            dal: An object conforming to the DataAccessLayer interface.
            notifier: A service to notify downstream systems of TGS finalization.
            audit_logger: The service for logging audit trails.
            workflow_manager: The service for managing workflow states.
        """
        self._dal = dal
        self._notifier = notifier
        self._audit_logger = audit_logger
        self._workflow_manager = workflow_manager

    def check_and_finalize(self, clinical_idea_id: int) -> None:
        """
        Checks if all concepts within a clinical idea have reached a consensus
        (either Include or Exclude). If so, it transitions the clinical idea's
        status to FINALIZED.

        This fulfills the implicit requirement from FRD PL3.1 and PL3.3 that
        the state machine must advance based on adjudication results.

        Args:
            clinical_idea_id: The ID of the clinical idea to check.
        """
        concept_statuses = self._dal.get_all_concept_statuses(clinical_idea_id)

        # An empty clinical idea is immediately ready for finalization.
        # Check if all concepts have moved out of the PENDING state.
        all_concepts_resolved = all(
            status.status != ConceptConsensusStatus.PENDING
            for status in concept_statuses
        )

        if all_concepts_resolved:
            # --- TGS Assembly (FRD AL5.2) ---
            # 1. Get the baseline "Intersection" concepts.
            intersection_ids = self._dal.get_intersection_concepts(clinical_idea_id)

            # 2. Get the "Delta" concepts that achieved CONSENSUS_INCLUDE.
            delta_include_ids = [
                status.concept_id
                for status in concept_statuses
                if status.status == ConceptConsensusStatus.CONSENSUS_INCLUDE
            ]

            # 3. Combine and create the final TGS definition.
            # Using a set handles potential duplicates between intersection and delta.
            final_tgs_ids = sorted(list(set(intersection_ids + delta_include_ids)))

            tgs_definition = TGS_Definition(
                clinical_idea_id=clinical_idea_id,
                concept_ids=final_tgs_ids,
            )

            # --- Auditing ---
            self._audit_logger.log_tgs_finalization(
                clinical_idea_id=clinical_idea_id,
                final_tgs_concept_ids=final_tgs_ids,
            )

            # --- TGS Persistence and State Locking (FRD AL5.3) ---
            self._dal.save_tgs(tgs_definition)
            self._workflow_manager.update_clinical_idea_status(
                clinical_idea_id, ClinicalIdeaStatus.FINALIZED
            )

            # --- Downstream Notification (FRD AL5.4) ---
            self._notifier.notify_tgs_ready(clinical_idea_id)
