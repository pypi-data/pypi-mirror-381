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
from typing import List

import pytest

from codeeval_adjudication_engine.consensus import ConsensusCalculator
from codeeval_adjudication_engine.models import (
    AdjudicationVote,
    AdjudicatorRoster,
    ConceptConsensusStatus,
    VoteDecision,
)


@pytest.fixture
def calculator() -> ConsensusCalculator:
    """Provides a ConsensusCalculator instance for testing."""
    return ConsensusCalculator()


@pytest.fixture
def active_roster() -> List[AdjudicatorRoster]:
    """Provides a sample roster of three active adjudicators."""
    return [
        AdjudicatorRoster(user_id="adjudicator_1", is_active=True),
        AdjudicatorRoster(user_id="adjudicator_2", is_active=True),
        AdjudicatorRoster(user_id="adjudicator_3", is_active=True),
    ]


def test_unanimous_include_yields_consensus_include(
    calculator: ConsensusCalculator, active_roster: List[AdjudicatorRoster]
):
    """
    Tests AL4.2: A concept is included ONLY IF 100% of the active
    Adjudicator Roster have submitted an active 'Include' vote.
    """
    concept_id = 101
    votes = [
        AdjudicationVote(
            "adjudicator_1",
            concept_id,
            VoteDecision.INCLUDE,
            timestamp=datetime.now(timezone.utc),
        ),
        AdjudicationVote(
            "adjudicator_2",
            concept_id,
            VoteDecision.INCLUDE,
            timestamp=datetime.now(timezone.utc),
        ),
        AdjudicationVote(
            "adjudicator_3",
            concept_id,
            VoteDecision.INCLUDE,
            timestamp=datetime.now(timezone.utc),
        ),
    ]

    result = calculator.calculate_consensus(concept_id, votes, active_roster)
    assert result == ConceptConsensusStatus.CONSENSUS_INCLUDE


def test_consensus_ignores_vote_if_marked_inactive(
    calculator: ConsensusCalculator, active_roster: List[AdjudicatorRoster]
):
    """
    Tests that a vote is ignored if its `is_active` flag is False,
    even if the adjudicator is active on the roster. This simulates a vote
    that has been invalidated by the OverrideManager.
    FRD AL7.4
    """
    concept_id = 109
    votes = [
        AdjudicationVote(
            "adjudicator_1",
            concept_id,
            VoteDecision.INCLUDE,
            timestamp=datetime.now(timezone.utc),
        ),
        AdjudicationVote(
            "adjudicator_2",
            concept_id,
            VoteDecision.INCLUDE,
            timestamp=datetime.now(timezone.utc),
        ),
        # This vote is from an active adjudicator but is marked inactive
        AdjudicationVote(
            "adjudicator_3",
            concept_id,
            VoteDecision.INCLUDE,
            is_active=False,  # The key part of this test
            timestamp=datetime.now(timezone.utc),
        ),
    ]

    # The result should be PENDING because the third required vote is inactive.
    result = calculator.calculate_consensus(concept_id, votes, active_roster)
    assert result == ConceptConsensusStatus.PENDING


def test_vote_from_inactive_adjudicator_is_ignored(
    calculator: ConsensusCalculator,
):
    """
    Tests AL7.4: Votes from an inactive adjudicator must be ignored.
    """
    concept_id = 105
    # adjudicator_3 is inactive, but the other two form a unanimous decision.
    roster = [
        AdjudicatorRoster(user_id="adjudicator_1", is_active=True),
        AdjudicatorRoster(user_id="adjudicator_2", is_active=True),
        AdjudicatorRoster(user_id="adjudicator_3", is_active=False),
    ]
    votes = [
        AdjudicationVote(
            "adjudicator_1",
            concept_id,
            VoteDecision.INCLUDE,
            timestamp=datetime.now(timezone.utc),
        ),
        AdjudicationVote(
            "adjudicator_2",
            concept_id,
            VoteDecision.INCLUDE,
            timestamp=datetime.now(timezone.utc),
        ),
        # This vote from the inactive user should be ignored
        AdjudicationVote(
            "adjudicator_3",
            concept_id,
            VoteDecision.EXCLUDE,
            timestamp=datetime.now(timezone.utc),
        ),
    ]

    result = calculator.calculate_consensus(concept_id, votes, roster)
    assert result == ConceptConsensusStatus.CONSENSUS_INCLUDE


def test_consensus_pending_if_active_adjudicator_has_not_voted(
    calculator: ConsensusCalculator,
):
    """
    Tests that consensus is PENDING if an active adjudicator's vote is missing,
    even if an inactive one has voted.
    """
    concept_id = 106
    roster = [
        AdjudicatorRoster(user_id="adjudicator_1", is_active=True),
        AdjudicatorRoster(
            user_id="adjudicator_2", is_active=True
        ),  # Active, but hasn't voted
        AdjudicatorRoster(user_id="adjudicator_3", is_active=False),
    ]
    votes = [
        AdjudicationVote(
            "adjudicator_1",
            concept_id,
            VoteDecision.INCLUDE,
            timestamp=datetime.now(timezone.utc),
        ),
        AdjudicationVote(
            "adjudicator_3",
            concept_id,
            VoteDecision.INCLUDE,
            timestamp=datetime.now(timezone.utc),
        ),
    ]

    result = calculator.calculate_consensus(concept_id, votes, roster)
    assert result == ConceptConsensusStatus.PENDING


def test_empty_vote_list_yields_pending(
    calculator: ConsensusCalculator, active_roster: List[AdjudicatorRoster]
):
    """
    Tests edge case: an empty list of votes results in PENDING.
    """
    result = calculator.calculate_consensus(107, [], active_roster)
    assert result == ConceptConsensusStatus.PENDING


def test_empty_roster_yields_pending(calculator: ConsensusCalculator):
    """
    Tests edge case: an empty roster results in PENDING.
    """
    votes = [
        AdjudicationVote(
            "adjudicator_1",
            108,
            VoteDecision.INCLUDE,
            timestamp=datetime.now(timezone.utc),
        )
    ]
    result = calculator.calculate_consensus(108, votes, [])
    assert result == ConceptConsensusStatus.PENDING


def test_one_exclude_vote_yields_consensus_exclude(
    calculator: ConsensusCalculator, active_roster: List[AdjudicatorRoster]
):
    """
    Tests AL4.4.1: If an 'Exclude' vote is received, the status can
    immediately be set to CONSENSUS_EXCLUDE.
    """
    concept_id = 102
    votes = [
        AdjudicationVote(
            "adjudicator_1",
            concept_id,
            VoteDecision.INCLUDE,
            timestamp=datetime.now(timezone.utc),
        ),
        AdjudicationVote(
            "adjudicator_2",
            concept_id,
            VoteDecision.EXCLUDE,
            timestamp=datetime.now(timezone.utc),
        ),
        AdjudicationVote(
            "adjudicator_3",
            concept_id,
            VoteDecision.INCLUDE,
            timestamp=datetime.now(timezone.utc),
        ),
    ]

    result = calculator.calculate_consensus(concept_id, votes, active_roster)
    assert result == ConceptConsensusStatus.CONSENSUS_EXCLUDE


def test_incomplete_votes_yields_pending(
    calculator: ConsensusCalculator, active_roster: List[AdjudicatorRoster]
):
    """
    Tests that consensus is PENDING if not all adjudicators have voted.
    """
    concept_id = 103
    votes = [
        AdjudicationVote(
            "adjudicator_1",
            concept_id,
            VoteDecision.INCLUDE,
            timestamp=datetime.now(timezone.utc),
        ),
        AdjudicationVote(
            "adjudicator_2",
            concept_id,
            VoteDecision.INCLUDE,
            timestamp=datetime.now(timezone.utc),
        ),
        # adjudicator_3 has not voted
    ]

    result = calculator.calculate_consensus(concept_id, votes, active_roster)
    assert result == ConceptConsensusStatus.PENDING


def test_votes_for_other_concepts_are_ignored(
    calculator: ConsensusCalculator, active_roster: List[AdjudicatorRoster]
):
    """
    Tests that the calculator correctly filters for votes matching the target
    concept_id.
    """
    concept_id = 104
    votes = [
        AdjudicationVote(
            "adjudicator_1",
            concept_id,
            VoteDecision.INCLUDE,
            timestamp=datetime.now(timezone.utc),
        ),
        AdjudicationVote(
            "adjudicator_2",
            concept_id,
            VoteDecision.INCLUDE,
            timestamp=datetime.now(timezone.utc),
        ),
        AdjudicationVote(
            "adjudicator_3",
            concept_id,
            VoteDecision.INCLUDE,
            timestamp=datetime.now(timezone.utc),
        ),
        # Add noise from another concept
        AdjudicationVote(
            "adjudicator_1",
            999,
            VoteDecision.EXCLUDE,
            timestamp=datetime.now(timezone.utc),
        ),
        AdjudicationVote(
            "adjudicator_2",
            999,
            VoteDecision.EXCLUDE,
            timestamp=datetime.now(timezone.utc),
        ),
    ]

    result = calculator.calculate_consensus(concept_id, votes, active_roster)
    assert result == ConceptConsensusStatus.CONSENSUS_INCLUDE
