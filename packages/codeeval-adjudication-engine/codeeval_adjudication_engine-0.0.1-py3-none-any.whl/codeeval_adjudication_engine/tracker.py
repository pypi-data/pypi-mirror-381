# Copyright (c) 2025-2026 Gowtham A Rao MD PhD. All Rights Reserved.
#
# This software is proprietary and dual-licensed.
# Licensed under the Prosperity Public License 3.0.0 (the "License").
# A copy of the license is available at https://prosperitylicense.com/versions/3.0.0
# For details, see the LICENSE file.
#
# Commercial use beyond a 30-day trial requires a separate license.
# Contact: rao@ohdsi.org

from collections import Counter

from .interfaces import DataAccessLayer
from .models import (
    AggregatedProgress,
    ConceptConsensusStatus,
    IndividualProgress,
)


class ProgressTracker:
    """
    Provides progress metrics for individuals and aggregated dashboards.
    Implements FRD AL6.
    """

    def __init__(self, dal: DataAccessLayer):
        """
        Initializes the ProgressTracker with a data access layer.

        Args:
            dal: An object conforming to the DataAccessLayer interface.
        """
        self._dal = dal

    def get_individual_progress(
        self, clinical_idea_id: int, user_id: str
    ) -> IndividualProgress:
        """
        Provides metrics for an individual adjudicator's progress.
        FRD AL6.1

        Args:
            clinical_idea_id: The ID of the clinical idea.
            user_id: The ID of the adjudicator.

        Returns:
            An object containing the reviewed and total counts.
        """
        user_votes = self._dal.get_votes_by_user(clinical_idea_id, user_id)
        all_concepts = self._dal.get_all_concepts_for_idea(clinical_idea_id)

        return IndividualProgress(
            reviewed_count=len(user_votes), total_count=len(all_concepts)
        )

    def get_aggregated_dashboard_metrics(
        self, clinical_idea_id: int
    ) -> AggregatedProgress:
        """
        Provides aggregated metrics for a Session Lead's dashboard.
        FRD AL6.2

        Args:
            clinical_idea_id: The ID of the clinical idea.

        Returns:
            An object containing aggregated counts for all concepts.
        """
        concept_statuses = self._dal.get_all_concept_statuses(clinical_idea_id)
        all_concepts = self._dal.get_all_concepts_for_idea(clinical_idea_id)

        status_counts = Counter(cs.status for cs in concept_statuses)

        total_concepts = len(all_concepts)
        include_count = status_counts[ConceptConsensusStatus.CONSENSUS_INCLUDE]
        exclude_count = status_counts[ConceptConsensusStatus.CONSENSUS_EXCLUDE]

        completed_count = include_count + exclude_count
        progress_percentage = (
            (completed_count / total_concepts) * 100.0 if total_concepts > 0 else 0.0
        )

        return AggregatedProgress(
            total_concepts=total_concepts,
            pending_count=status_counts[ConceptConsensusStatus.PENDING],
            consensus_include_count=include_count,
            consensus_exclude_count=exclude_count,
            overall_progress_percentage=progress_percentage,
        )
