# Copyright (c) 2025-2026 Gowtham A Rao MD PhD. All Rights Reserved.
#
# This software is proprietary and dual-licensed.
# Licensed under the Prosperity Public License 3.0.0 (the "License").
# A copy of the license is available at https://prosperitylicense.com/versions/3.0.0
# For details, see the LICENSE file.
#
# Commercial use beyond a 30-day trial requires a separate license.
# Contact: rao@ohdsi.org

from contextlib import contextmanager
from typing import Dict, Generator, List, Optional
from unittest.mock import MagicMock

from codeeval_adjudication_engine.interfaces import (
    AuditLogger,
    DataAccessLayer,
    TGSFinalizationNotifier,
)
from codeeval_adjudication_engine.models import (
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
from codeeval_adjudication_engine.workflow_manager import WorkflowManager


class MockWorkflowManager(WorkflowManager):
    """
    A mock implementation of the WorkflowManager for isolated testing.
    This class uses MagicMock to allow spying on method calls.
    """

    def __init__(self, dal: DataAccessLayer):
        super().__init__(dal)
        # Spy on methods to track calls while preserving real logic
        self.update_clinical_idea_status = MagicMock(
            wraps=self.update_clinical_idea_status
        )
        self.modify_roster = MagicMock(wraps=self.modify_roster)
        self.get_roster = MagicMock(wraps=self.get_roster)


class MockDataAccessLayer(DataAccessLayer):
    """
    A mock implementation of the DataAccessLayer for isolated testing.
    This class allows for predictable testing of business logic by providing
    pre-canned data without requiring a real database connection. It implements
    the full DataAccessLayer interface.
    """

    def __init__(
        self,
        votes: Optional[List[AdjudicationVote]] = None,
        concepts_by_idea: Optional[Dict[int, List[Concept]]] = None,
        concept_statuses: Optional[List[ConceptStatus]] = None,
        roster: Optional[List[AdjudicatorRoster]] = None,
        idea_status: Optional[ClinicalIdeaStatus] = None,
        intersection_concepts: Optional[List[int]] = None,
        clinical_idea_descriptions: Optional[Dict[int, str]] = None,
    ):
        self._votes = votes or []
        self._concepts_by_idea = concepts_by_idea or {}
        self._concept_statuses: Dict[int, ConceptStatus] = {
            cs.concept_id: cs for cs in (concept_statuses or [])
        }
        self._roster = roster or []
        self._idea_status = idea_status or ClinicalIdeaStatus.PENDING
        self._intersection_concepts = intersection_concepts or []
        self._clinical_idea_descriptions = clinical_idea_descriptions or {}
        self.saved_tgs: Optional[TGS_Definition] = None
        self.override_audit_log_entries: List[OverrideAuditLog] = []
        self.vote_audit_log_entries: List[VoteAuditLog] = []
        self.tgs_finalization_audit_log_entries: List[TGSFinalizationAuditLog] = []
        self.transaction_context = MagicMock()

    # --- Transaction Management ---
    @contextmanager
    def transaction(self) -> Generator[None, None, None]:
        with self.transaction_context:
            yield

    # --- Data Retrieval ---
    def get_votes_by_user(
        self, clinical_idea_id: int, user_id: str
    ) -> List[AdjudicationVote]:
        return [vote for vote in self._votes if vote.user_id == user_id]

    def get_clinical_idea_description(self, clinical_idea_id: int) -> str:
        """Retrieves the mock description for a given clinical idea."""
        return self._clinical_idea_descriptions.get(
            clinical_idea_id, "Description not found"
        )

    def get_all_concepts_for_idea(self, clinical_idea_id: int) -> List[Concept]:
        return self._concepts_by_idea.get(clinical_idea_id, [])

    def get_all_concept_statuses(self, clinical_idea_id: int) -> List[ConceptStatus]:
        return list(self._concept_statuses.values())

    def get_active_roster(self, clinical_idea_id: int) -> List[AdjudicatorRoster]:
        return self._roster

    def get_clinical_idea_status(self, clinical_idea_id: int) -> ClinicalIdeaStatus:
        return self._idea_status

    def get_concept_status_for_update(self, concept_id: int) -> ConceptStatus:
        if concept_id not in self._concept_statuses:
            self._concept_statuses[concept_id] = ConceptStatus(concept_id=concept_id)
        return self._concept_statuses[concept_id]

    def get_all_concept_statuses_for_update(
        self, clinical_idea_id: int
    ) -> List[ConceptStatus]:
        # In a real implementation, this would lock the rows.
        # For the mock, it's equivalent to the non-locking version.
        return self.get_all_concept_statuses(clinical_idea_id)

    def get_all_votes(self, clinical_idea_id: int) -> List[AdjudicationVote]:
        return self._votes

    def get_vote_by_user_and_concept(
        self, user_id: str, concept_id: int
    ) -> Optional[AdjudicationVote]:
        """Finds a specific vote in the mock data store."""
        for vote in self._votes:
            if vote.user_id == user_id and vote.concept_id == concept_id:
                return vote
        return None

    def get_intersection_concepts(self, clinical_idea_id: int) -> List[int]:
        return self._intersection_concepts

    # --- Data Persistence ---
    def update_clinical_idea_status(
        self, clinical_idea_id: int, status: ClinicalIdeaStatus
    ) -> None:
        self._idea_status = status

    def create_vote(self, vote: AdjudicationVote) -> None:
        """Adds a new vote to the in-memory list."""
        self._votes.append(vote)

    def update_vote(self, vote: AdjudicationVote) -> None:
        """Finds and updates an existing vote in the in-memory list."""
        for i, existing_vote in enumerate(self._votes):
            if (
                existing_vote.user_id == vote.user_id
                and existing_vote.concept_id == vote.concept_id
            ):
                self._votes[i] = vote
                return

    def update_concept_status(
        self, concept_id: int, status: ConceptConsensusStatus
    ) -> None:
        if concept_id in self._concept_statuses:
            self._concept_statuses[concept_id].status = status
        else:
            self._concept_statuses[concept_id] = ConceptStatus(
                concept_id=concept_id, status=status
            )

    def save_tgs(self, tgs: TGS_Definition) -> None:
        self.saved_tgs = tgs

    def modify_roster_status(
        self, clinical_idea_id: int, user_id: str, is_active: bool
    ) -> None:
        """Finds the adjudicator on the roster and updates their status."""
        for adj in self._roster:
            if adj.user_id == user_id:
                adj.is_active = is_active
                break

    def invalidate_votes(self, clinical_idea_id: int, user_id: str) -> None:
        """Finds all votes by a user and marks them as inactive."""
        for vote in self._votes:
            if vote.user_id == user_id:
                vote.is_active = False

    def create_override_audit_log(self, log_entry: OverrideAuditLog) -> None:
        """Appends the audit log entry to the in-memory list for inspection."""
        self.override_audit_log_entries.append(log_entry)

    def create_vote_audit_log(self, log_entry: VoteAuditLog) -> None:
        """Appends the vote audit log entry to the in-memory list for inspection."""
        self.vote_audit_log_entries.append(log_entry)

    def create_tgs_finalization_audit_log(
        self, log_entry: TGSFinalizationAuditLog
    ) -> None:
        """
        Appends the TGS finalization audit log entry to the in-memory list for
        inspection.
        """
        self.tgs_finalization_audit_log_entries.append(log_entry)


class MockTGSFinalizationNotifier(TGSFinalizationNotifier):
    """
    A mock implementation of the TGSFinalizationNotifier for testing.
    This class records notifications so that tests can assert whether the
    downstream notification was correctly triggered.
    """

    def __init__(self):
        self.notified_ideas: List[int] = []

    def notify_tgs_ready(self, clinical_idea_id: int) -> None:
        """Records the clinical idea ID that was finalized."""
        self.notified_ideas.append(clinical_idea_id)


class MockAuditLogger(AuditLogger):
    """
    A mock implementation of the AuditLogger for testing.
    This class records calls to its methods so that tests can assert whether
    the auditing functionality was correctly triggered.
    """

    def __init__(self):
        self.logged_actions: List[Dict] = []

    def log_override_action(
        self,
        session_lead_id: str,
        affected_adjudicator_id: str,
        action: str,
        clinical_idea_id: int,
    ) -> None:
        """Records the details of the override action."""
        self.logged_actions.append(
            {
                "type": "OVERRIDE",
                "session_lead_id": session_lead_id,
                "affected_adjudicator_id": affected_adjudicator_id,
                "action": action,
                "clinical_idea_id": clinical_idea_id,
            }
        )

    def log_vote_action(
        self,
        user_id: str,
        concept_id: int,
        clinical_idea_id: int,
        decision: VoteDecision,
    ) -> None:
        """Records the details of the vote action."""
        self.logged_actions.append(
            {
                "type": "VOTE",
                "user_id": user_id,
                "concept_id": concept_id,
                "clinical_idea_id": clinical_idea_id,
                "decision": decision,
            }
        )

    def log_tgs_finalization(
        self,
        clinical_idea_id: int,
        final_tgs_concept_ids: List[int],
    ) -> None:
        """Records the details of the TGS finalization event."""
        self.logged_actions.append(
            {
                "type": "TGS_FINALIZATION",
                "clinical_idea_id": clinical_idea_id,
                "final_tgs_concept_ids": final_tgs_concept_ids,
            }
        )
