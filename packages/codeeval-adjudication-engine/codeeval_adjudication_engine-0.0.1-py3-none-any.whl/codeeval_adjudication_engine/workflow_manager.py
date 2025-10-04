# Copyright (c) 2025-2026 Gowtham A Rao MD PhD. All Rights Reserved.
#
# This software is proprietary and dual-licensed.
# Licensed under the Prosperity Public License 3.0.0 (the "License").
# A copy of the license is available at https://prosperitylicense.com/versions/3.0.0
# For details, see the LICENSE file.
#
# Commercial use beyond a 30-day trial requires a separate license.
# Contact: rao@ohdsi.org

from typing import List

from .interfaces import DataAccessLayer
from .models import (
    AdjudicatorRoster,
    ClinicalIdeaStatus,
    ConceptConsensusStatus,
    InvalidStateError,
)


class WorkflowManager:
    """
    Manages the overall adjudication workflow, including authorization and state
    transitions. Implements FRD AL1.
    """

    def __init__(self, dal: DataAccessLayer):
        """
        Initializes the WorkflowManager with a data access layer.

        Args:
            dal: An object conforming to the DataAccessLayer interface.
        """
        self._dal = dal

    def is_adjudicator_authorized(self, user_id: str, clinical_idea_id: int) -> bool:
        """
        Verifies if an adjudicator is actively assigned to the clinical idea.
        FRD AL1.1: Domain-Specific Authorization.

        Args:
            user_id: The ID of the user to verify.
            clinical_idea_id: The ID of the clinical idea.

        Returns:
            True if the user is an active adjudicator for the clinical idea,
            False otherwise.
        """
        active_roster = self._dal.get_active_roster(clinical_idea_id)
        return any(
            adjudicator.user_id == user_id and adjudicator.is_active
            for adjudicator in active_roster
        )

    def start_adjudication(self, clinical_idea_id: int) -> None:
        """
        Transitions the status of a Clinical Idea from PENDING to IN_PROGRESS.
        FRD AL1.2: Clinical Idea State Management.

        This method contains the business logic for starting the adjudication process.
        It is idempotent; it will not raise an error if the process has already
        started.

        Args:
            clinical_idea_id: The ID of the clinical idea to start.

        Raises:
            InvalidStateError: If the clinical idea is in a non-transitional
                             state, such as FINALIZED.
        """
        self.update_clinical_idea_status(
            clinical_idea_id, ClinicalIdeaStatus.IN_PROGRESS
        )

    def update_clinical_idea_status(
        self, clinical_idea_id: int, new_status: ClinicalIdeaStatus
    ) -> None:
        """
        Manages the state transitions of a Clinical Idea.

        This method centralizes state management logic, ensuring that all
        transitions are valid according to the business rules. For example,
        an idea can move from IN_PROGRESS to FINALIZED, but not from
        FINALIZED back to IN_PROGRESS.

        Args:
            clinical_idea_id: The ID of the clinical idea to update.
            new_status: The target status.

        Raises:
            InvalidStateError: If the requested state transition is not allowed.
        """
        current_status = self._dal.get_clinical_idea_status(clinical_idea_id)
        if current_status == new_status:
            return  # The operation is idempotent.

        # Define valid state transitions.
        # Key: current_status, Value: set of valid next statuses.
        valid_transitions = {
            ClinicalIdeaStatus.PENDING: {ClinicalIdeaStatus.IN_PROGRESS},
            ClinicalIdeaStatus.IN_PROGRESS: {ClinicalIdeaStatus.FINALIZED},
            ClinicalIdeaStatus.FINALIZED: set(),  # No transitions out of FINALIZED.
        }

        if new_status not in valid_transitions.get(current_status, set()):
            raise InvalidStateError(
                f"Invalid state transition for clinical idea {clinical_idea_id} "
                f"from '{current_status.name}' to '{new_status.name}'."
            )

        self._dal.update_clinical_idea_status(clinical_idea_id, new_status)

    def update_concept_status(
        self,
        clinical_idea_id: int,
        concept_id: int,
        new_status: ConceptConsensusStatus,
    ) -> None:
        """
        Manages the state of an individual concept.
        FRD AL1.3: Concept State Management.

        Before updating a concept's status, it validates that the parent
        clinical idea is not finalized.

        Args:
            clinical_idea_id: The ID of the parent clinical idea.
            concept_id: The ID of the concept to update.
            new_status: The new status to set for the concept.

        Raises:
            InvalidStateError: If the clinical idea is already FINALIZED.
        """
        # FRD AL3.2: Validate the Clinical Idea State is not FINALIZED.
        idea_status = self._dal.get_clinical_idea_status(clinical_idea_id)
        if idea_status == ClinicalIdeaStatus.FINALIZED:
            raise InvalidStateError(
                f"Cannot update concept {concept_id} status; clinical idea "
                f"{clinical_idea_id} is already finalized."
            )

        # Persist the change via the Data Access Layer.
        self._dal.update_concept_status(concept_id, new_status)

    def get_roster(self, clinical_idea_id: int) -> List[AdjudicatorRoster]:
        """
        Retrieves the active adjudicator roster for a given clinical idea.
        This method centralizes access to the roster as required by FRD AL1.4.

        Args:
            clinical_idea_id: The ID of the clinical idea.

        Returns:
            A list of AdjudicatorRoster objects.
        """
        return self._dal.get_active_roster(clinical_idea_id)

    def modify_roster(
        self,
        clinical_idea_id: int,
        user_id_to_modify: str,
        new_active_status: bool,
    ) -> None:
        """
        Modifies an adjudicator's status on the roster and invalidates their
        votes if they are being deactivated.
        This centralizes roster modification logic per FRD AL1.4.

        Args:
            clinical_idea_id: The ID of the clinical idea.
            user_id_to_modify: The adjudicator's user ID.
            new_active_status: The new active status to set.
        """
        self._dal.modify_roster_status(
            clinical_idea_id, user_id_to_modify, new_active_status
        )
        if not new_active_status:
            self._dal.invalidate_votes(clinical_idea_id, user_id_to_modify)
