# Copyright (c) 2025-2026 Gowtham A Rao MD PhD. All Rights Reserved.
#
# This software is proprietary and dual-licensed.
# Licensed under the Prosperity Public License 3.0.0 (the "License").
# A copy of the license is available at https://prosperitylicense.com/versions/3.0.0
# For details, see the LICENSE file.
#
# Commercial use beyond a 30-day trial requires a separate license.
# Contact: rao@ohdsi.org

from typing import List, Set

from .models import (
    AdjudicationVote,
    AdjudicatorRoster,
    ConceptConsensusStatus,
    VoteDecision,
)


class ConsensusCalculator:
    """
    Implements the Unanimity consensus rule based on the active Adjudicator Roster.
    Adheres to FRD requirements AL4.2, AL4.3, and AL4.4.
    """

    def calculate_consensus(
        self,
        concept_id: int,
        all_votes: List[AdjudicationVote],
        active_roster: List[AdjudicatorRoster],
    ) -> ConceptConsensusStatus:
        """
        Calculates the consensus status for a single concept based on the
        Unanimity Rule.

        Args:
            concept_id: The ID of the concept being evaluated.
            all_votes: A list of all votes cast for any concept.
            active_roster: The list of all adjudicators assigned to the
                clinical idea, including their active status.

        Returns:
            The calculated consensus status for the concept.
        """
        active_adjudicator_ids: Set[str] = {
            roster_member.user_id
            for roster_member in active_roster
            if roster_member.is_active
        }

        if not active_adjudicator_ids:
            # If there are no active adjudicators, no consensus can be reached.
            return ConceptConsensusStatus.PENDING

        # Filter for active votes concerning the specific concept.
        # This fulfills the requirement to ignore invalidated votes (FRD AL7.4).
        active_votes_for_concept = [
            vote
            for vote in all_votes
            if vote.concept_id == concept_id and vote.is_active
        ]

        # Check for any "Exclude" vote from an active adjudicator (AL4.4.1)
        for vote in active_votes_for_concept:
            if (
                vote.user_id in active_adjudicator_ids
                and vote.decision == VoteDecision.EXCLUDE
            ):
                return ConceptConsensusStatus.CONSENSUS_EXCLUDE

        # Check for Unanimity "Include" (AL4.2)
        include_voter_ids: Set[str] = {
            vote.user_id
            for vote in active_votes_for_concept
            if vote.decision == VoteDecision.INCLUDE
        }

        # The set of voters must be exactly the set of active adjudicators.
        if include_voter_ids == active_adjudicator_ids:
            return ConceptConsensusStatus.CONSENSUS_INCLUDE

        return ConceptConsensusStatus.PENDING
