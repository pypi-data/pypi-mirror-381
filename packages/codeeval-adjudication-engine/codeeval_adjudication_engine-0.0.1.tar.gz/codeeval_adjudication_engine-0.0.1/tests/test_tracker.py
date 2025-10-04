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

import pytest

from codeeval_adjudication_engine.models import (
    AdjudicationVote,
    Concept,
    ConceptConsensusStatus,
    ConceptStatus,
    VoteDecision,
)
from codeeval_adjudication_engine.tracker import ProgressTracker
from tests.mocks import MockDataAccessLayer

# --- Test Data ---

CONCEPTS_FIXTURE = [
    Concept(1, "A", "Desc A", 1, []),
    Concept(2, "B", "Desc B", 2, []),
    Concept(3, "C", "Desc C", 3, []),
    Concept(4, "D", "Desc D", 1, []),
    Concept(5, "E", "Desc E", 2, []),
]

VOTES_FIXTURE = [
    AdjudicationVote(
        "user1", 1, VoteDecision.INCLUDE, timestamp=datetime.now(timezone.utc)
    ),
    AdjudicationVote(
        "user1", 2, VoteDecision.EXCLUDE, timestamp=datetime.now(timezone.utc)
    ),
    AdjudicationVote(
        "user2", 1, VoteDecision.INCLUDE, timestamp=datetime.now(timezone.utc)
    ),
    AdjudicationVote(
        "user2", 3, VoteDecision.INCLUDE, timestamp=datetime.now(timezone.utc)
    ),
    AdjudicationVote(
        "user2", 4, VoteDecision.EXCLUDE, timestamp=datetime.now(timezone.utc)
    ),
]

STATUS_FIXTURE = [
    ConceptStatus(1, ConceptConsensusStatus.CONSENSUS_INCLUDE),
    ConceptStatus(2, ConceptConsensusStatus.PENDING),
    ConceptStatus(3, ConceptConsensusStatus.PENDING),
    ConceptStatus(4, ConceptConsensusStatus.CONSENSUS_EXCLUDE),
    ConceptStatus(5, ConceptConsensusStatus.PENDING),
]

# --- Test Cases ---


class TestProgressTracker:
    """Unit tests for the ProgressTracker service."""

    def test_get_individual_progress_with_votes(self):
        """
        Tests FRD AL6.1: Individual progress for a user with some votes.
        """
        mock_dal = MockDataAccessLayer(
            votes=VOTES_FIXTURE, concepts_by_idea={1: CONCEPTS_FIXTURE}
        )
        tracker = ProgressTracker(dal=mock_dal)

        progress = tracker.get_individual_progress(clinical_idea_id=1, user_id="user1")

        assert progress.reviewed_count == 2
        assert progress.total_count == 5

    def test_get_individual_progress_no_votes(self):
        """
        Tests FRD AL6.1: Individual progress for a user with no votes.
        """
        mock_dal = MockDataAccessLayer(
            votes=VOTES_FIXTURE, concepts_by_idea={1: CONCEPTS_FIXTURE}
        )
        tracker = ProgressTracker(dal=mock_dal)

        progress = tracker.get_individual_progress(
            clinical_idea_id=1, user_id="user_with_no_votes"
        )

        assert progress.reviewed_count == 0
        assert progress.total_count == 5

    def test_get_individual_progress_no_concepts(self):
        """
        Tests FRD AL6.1: Edge case with zero concepts in the clinical idea.
        """
        mock_dal = MockDataAccessLayer(votes=VOTES_FIXTURE, concepts_by_idea={1: []})
        tracker = ProgressTracker(dal=mock_dal)

        progress = tracker.get_individual_progress(clinical_idea_id=1, user_id="user1")

        assert progress.reviewed_count == 2
        assert progress.total_count == 0

    def test_get_aggregated_dashboard_metrics(self):
        """
        Tests FRD AL6.2: Aggregated progress with a mix of statuses.
        """
        mock_dal = MockDataAccessLayer(
            concepts_by_idea={1: CONCEPTS_FIXTURE}, concept_statuses=STATUS_FIXTURE
        )
        tracker = ProgressTracker(dal=mock_dal)

        metrics = tracker.get_aggregated_dashboard_metrics(clinical_idea_id=1)

        assert metrics.total_concepts == 5
        assert metrics.pending_count == 3
        assert metrics.consensus_include_count == 1
        assert metrics.consensus_exclude_count == 1
        assert metrics.overall_progress_percentage == pytest.approx(40.0)

    def test_get_aggregated_dashboard_metrics_no_concepts(self):
        """
        Tests FRD AL6.2: Edge case with zero concepts, expecting 0% progress.
        """
        mock_dal = MockDataAccessLayer(concepts_by_idea={1: []}, concept_statuses=[])
        tracker = ProgressTracker(dal=mock_dal)

        metrics = tracker.get_aggregated_dashboard_metrics(clinical_idea_id=1)

        assert metrics.total_concepts == 0
        assert metrics.pending_count == 0
        assert metrics.consensus_include_count == 0
        assert metrics.consensus_exclude_count == 0
        assert metrics.overall_progress_percentage == 0.0

    def test_get_aggregated_dashboard_metrics_all_pending(self):
        """
        Tests FRD AL6.2: Case where all concepts are pending, expecting 0% progress.
        """
        statuses = [
            ConceptStatus(c.concept_id, ConceptConsensusStatus.PENDING)
            for c in CONCEPTS_FIXTURE
        ]
        mock_dal = MockDataAccessLayer(
            concepts_by_idea={1: CONCEPTS_FIXTURE}, concept_statuses=statuses
        )
        tracker = ProgressTracker(dal=mock_dal)

        metrics = tracker.get_aggregated_dashboard_metrics(clinical_idea_id=1)

        assert metrics.total_concepts == 5
        assert metrics.pending_count == 5
        assert metrics.consensus_include_count == 0
        assert metrics.consensus_exclude_count == 0
        assert metrics.overall_progress_percentage == 0.0

    def test_get_aggregated_dashboard_metrics_all_complete(self):
        """
        Tests FRD AL6.2: Case where all concepts are completed, expecting 100% progress.
        """
        statuses = [
            ConceptStatus(1, ConceptConsensusStatus.CONSENSUS_INCLUDE),
            ConceptStatus(2, ConceptConsensusStatus.CONSENSUS_EXCLUDE),
            ConceptStatus(3, ConceptConsensusStatus.CONSENSUS_INCLUDE),
            ConceptStatus(4, ConceptConsensusStatus.CONSENSUS_EXCLUDE),
            ConceptStatus(5, ConceptConsensusStatus.CONSENSUS_INCLUDE),
        ]
        mock_dal = MockDataAccessLayer(
            concepts_by_idea={1: CONCEPTS_FIXTURE}, concept_statuses=statuses
        )
        tracker = ProgressTracker(dal=mock_dal)

        metrics = tracker.get_aggregated_dashboard_metrics(clinical_idea_id=1)

        assert metrics.total_concepts == 5
        assert metrics.pending_count == 0
        assert metrics.consensus_include_count == 3
        assert metrics.consensus_exclude_count == 2
        assert metrics.overall_progress_percentage == 100.0
