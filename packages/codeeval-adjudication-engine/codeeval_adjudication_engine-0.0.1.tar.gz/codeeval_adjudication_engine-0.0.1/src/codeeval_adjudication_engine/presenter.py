# Copyright (c) 2025-2026 Gowtham A Rao MD PhD. All Rights Reserved.
#
# This software is proprietary and dual-licensed.
# Licensed under the Prosperity Public License 3.0.0 (the "License").
# A copy of the license is available at https://prosperitylicense.com/versions/3.0.0
# For details, see the LICENSE file.
#
# Commercial use beyond a 30-day trial requires a separate license.
# Contact: rao@ohdsi.org

import random

from .interfaces import DataAccessLayer
from .models import AdjudicationDataPackage, BlindedConceptView, UserContext


class DataPresenter:
    """
    Manages the blinded presentation and randomization of concepts for adjudication,
    adhering to FRD requirements AL2.
    """

    def __init__(self, dal: DataAccessLayer):
        """
        Initializes the DataPresenter with a data access layer.

        Args:
            dal: An object conforming to the DataAccessLayer interface.
        """
        self._dal = dal

    def get_concepts_for_review(
        self,
        clinical_idea_id: int,
        user_context: UserContext,
    ) -> AdjudicationDataPackage:
        """
        Retrieves, filters, and randomizes concepts for an adjudication session.

        This method fulfills FRD requirements:
        - AL2.3: Retrieves the concept list.
        - AL2.1: Actively filters the concept pool to produce the BlindedConceptView.
        - AL2.2: Randomizes the sequence of concepts using a session-specific seed.
        - AL2.4: Provides the standardized 'Clinical Description' for context.

        Args:
            clinical_idea_id: The ID of the clinical idea being reviewed.
            user_context: The user's session context, which must contain the
                          `session_rng_seed` for randomization.

        Returns:
            An `AdjudicationDataPackage` containing the clinical idea's description
            and the list of sanitized, randomized concepts for review.
        """
        # Fetch data from the DAL
        description = self._dal.get_clinical_idea_description(clinical_idea_id)
        concepts = self._dal.get_all_concepts_for_idea(clinical_idea_id)

        # Create a mutable copy to avoid side effects on the original list.
        concepts_copy = list(concepts)

        # Use a dedicated Random instance with the session-specific seed to ensure
        # deterministic shuffling without interfering with the global random state.
        session_randomizer = random.Random(user_context.session_rng_seed)
        session_randomizer.shuffle(concepts_copy)

        # Transform the shuffled concepts into the sanitized BlindedConceptView,
        # explicitly excluding 'agreement_level' and 'contributing_arms' as
        # mandated by the blinding protocol (FRD AL2.1.1).
        blinded_concepts = [
            BlindedConceptView(
                concept_id=c.concept_id,
                name=c.name,
                description=c.description,
            )
            for c in concepts_copy
        ]

        # Package the description and concepts together
        return AdjudicationDataPackage(
            clinical_idea_description=description,
            concepts_for_review=blinded_concepts,
        )
