# Copyright (c) 2025-2026 Gowtham A Rao MD PhD. All Rights Reserved.
#
# This software is proprietary and dual-licensed.
# Licensed under the Prosperity Public License 3.0.0 (the "License").
# A copy of the license is available at https://prosperitylicense.com/versions/3.0.0
# For details, see the LICENSE file.
#
# Commercial use beyond a 30-day trial requires a separate license.
# Contact: rao@ohdsi.org

from abc import ABC, abstractmethod
from contextlib import contextmanager
from typing import Generator, List

from .models import (
    AdjudicationVote,
    AdjudicatorRoster,
    ClinicalIdeaStatus,
    Concept,
    ConceptConsensusStatus,
    ConceptStatus,
    OverrideAuditLog,
    TGS_Definition,
    TGSFinalizationAuditLog,
    VoteAuditLog,
    VoteDecision,
)


class DataAccessLayer(ABC):
    """
    Abstract interface for the Data Access Layer (DAL).

    Defines the contract for data persistence and retrieval operations, decoupling
    the business logic from the underlying database implementation as mandated
    by FRD A3.
    """

    # === Transaction Management (FRD AL3.5) ===
    @abstractmethod
    @contextmanager
    def transaction(self) -> Generator[None, None, None]:
        """Provides a transactional context."""
        yield

    # === Data Retrieval ===
    @abstractmethod
    def get_votes_by_user(
        self, clinical_idea_id: int, user_id: str
    ) -> List[AdjudicationVote]:
        """Retrieves all votes cast by a specific user for a given clinical idea."""
        pass

    @abstractmethod
    def get_clinical_idea_description(self, clinical_idea_id: int) -> str:
        """Retrieves the description for a given clinical idea."""
        pass

    @abstractmethod
    def get_all_concept_statuses_for_update(
        self, clinical_idea_id: int
    ) -> List[ConceptStatus]:
        """Retrieves all concept statuses for an idea, acquiring a pessimistic lock."""
        pass

    @abstractmethod
    def get_all_concepts_for_idea(self, clinical_idea_id: int) -> List[Concept]:
        """Retrieves all concepts associated with a given clinical idea."""
        pass

    @abstractmethod
    def get_all_concept_statuses(self, clinical_idea_id: int) -> List[ConceptStatus]:
        """Retrieves the consensus status for all concepts in a given clinical idea."""
        pass

    @abstractmethod
    def get_active_roster(self, clinical_idea_id: int) -> List[AdjudicatorRoster]:
        """Retrieves the active adjudicator roster for a given clinical idea."""
        pass

    @abstractmethod
    def get_clinical_idea_status(self, clinical_idea_id: int) -> ClinicalIdeaStatus:
        """Retrieves the current status of a given clinical idea."""
        pass

    @abstractmethod
    def get_concept_status_for_update(self, concept_id: int) -> ConceptStatus:
        """Retrieves a concept's status, acquiring a pessimistic lock."""
        pass

    @abstractmethod
    def get_all_votes(self, clinical_idea_id: int) -> List[AdjudicationVote]:
        """Retrieves all votes for a given clinical idea."""
        pass

    @abstractmethod
    def get_vote_by_user_and_concept(
        self, user_id: str, concept_id: int
    ) -> AdjudicationVote | None:
        """Retrieves a single vote for a specific user and concept, if one exists."""
        pass

    @abstractmethod
    def get_intersection_concepts(self, clinical_idea_id: int) -> List[int]:
        """Retrieves concept IDs from the intersection set for TGS construction."""
        pass

    # === Data Persistence ===
    @abstractmethod
    def update_clinical_idea_status(
        self, clinical_idea_id: int, status: ClinicalIdeaStatus
    ) -> None:
        """Updates the status of a given clinical idea."""
        pass

    @abstractmethod
    def create_vote(self, vote: AdjudicationVote) -> None:
        """Creates a new vote record."""
        pass

    @abstractmethod
    def update_vote(self, vote: AdjudicationVote) -> None:
        """Updates an existing vote record."""
        pass

    @abstractmethod
    def update_concept_status(
        self, concept_id: int, status: ConceptConsensusStatus
    ) -> None:
        """Updates the consensus status of a single concept."""
        pass

    @abstractmethod
    def save_tgs(self, tgs: TGS_Definition) -> None:
        """Persists the final True Gold Standard."""
        pass

    @abstractmethod
    def modify_roster_status(
        self, clinical_idea_id: int, user_id: str, is_active: bool
    ) -> None:
        """Activates or deactivates an adjudicator on the roster."""
        pass

    @abstractmethod
    def invalidate_votes(self, clinical_idea_id: int, user_id: str) -> None:
        """Logically invalidates all votes by a specific user for a clinical idea."""
        pass

    @abstractmethod
    def create_override_audit_log(self, log_entry: OverrideAuditLog) -> None:
        """Creates a persistent record of an override action."""
        pass

    @abstractmethod
    def create_vote_audit_log(self, log_entry: VoteAuditLog) -> None:
        """Creates a persistent record of a vote action."""
        pass

    @abstractmethod
    def create_tgs_finalization_audit_log(
        self, log_entry: TGSFinalizationAuditLog
    ) -> None:
        """Creates a persistent record of a TGS finalization event."""
        pass


class TGSFinalizationNotifier(ABC):
    """
    Abstract interface for a service that notifies downstream systems when a
    True Gold Standard (TGS) has been finalized.

    This fulfills FRD AL5.4, decoupling the adjudication engine from the
    downstream consumer (e.g., the sap_engine).
    """

    @abstractmethod
    def notify_tgs_ready(self, clinical_idea_id: int) -> None:
        """
        Signals that the TGS for a given clinical idea is finalized and ready
        for consumption.

        Args:
            clinical_idea_id: The ID of the finalized clinical idea.
        """
        pass


class AuditLogger(ABC):
    """
    Abstract interface for a service that logs security-sensitive audit events,
    such as operational overrides.

    This fulfills FRD AL7.6 and NFR-AL5, ensuring all critical actions are
    rigorously audited.
    """

    @abstractmethod
    def log_override_action(
        self,
        session_lead_id: str,
        affected_adjudicator_id: str,
        action: str,
        clinical_idea_id: int,
    ) -> None:
        """
        Logs the details of an operational override action.

        Args:
            session_lead_id: The ID of the Session Lead performing the override.
            affected_adjudicator_id: The ID of the adjudicator being modified.
            action: A description of the action taken (e.g., "DEACTIVATE", "ACTIVATE").
            clinical_idea_id: The ID of the clinical idea being affected.
        """
        pass

    @abstractmethod
    def log_vote_action(
        self,
        user_id: str,
        concept_id: int,
        clinical_idea_id: int,
        decision: VoteDecision,
    ) -> None:
        """
        Logs the details of a vote action.

        Args:
            user_id: The ID of the user casting the vote.
            concept_id: The ID of the concept being voted on.
            clinical_idea_id: The ID of the associated clinical idea.
            decision: The decision made in the vote (e.g., INCLUDE, EXCLUDE).
        """
        pass

    @abstractmethod
    def log_tgs_finalization(
        self,
        clinical_idea_id: int,
        final_tgs_concept_ids: List[int],
    ) -> None:
        """
        Logs the details of a TGS finalization event.

        Args:
            clinical_idea_id: The ID of the clinical idea being finalized.
            final_tgs_concept_ids: The final list of concept IDs in the TGS.
        """
        pass
