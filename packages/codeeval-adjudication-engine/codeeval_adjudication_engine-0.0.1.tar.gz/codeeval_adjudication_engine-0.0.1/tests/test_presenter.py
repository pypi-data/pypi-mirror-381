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
from unittest.mock import patch

import pytest

from codeeval_adjudication_engine.models import (
    AdjudicationDataPackage,
    BlindedConceptView,
    Concept,
    UserContext,
)
from codeeval_adjudication_engine.presenter import DataPresenter

from .mocks import MockDataAccessLayer


@pytest.fixture
def sample_concepts() -> List[Concept]:
    """Provides a sample list of Concept objects for testing."""
    return [
        Concept(1, "Heart Attack", "Clinical finding", 3, ["ArmA", "ArmB", "ArmC"]),
        Concept(2, "Diabetes", "Disorder", 2, ["ArmA", "ArmB"]),
        Concept(3, "Hypertension", "Disorder", 1, ["ArmC"]),
        Concept(4, "Fever", "Clinical finding", 2, ["ArmB", "ArmD"]),
    ]


def test_dal_get_all_concepts_is_called(sample_concepts: List[Concept]):
    """
    Validates that the DataPresenter correctly calls the DAL to fetch concepts.
    This replaces the old 'test_input_list_is_not_mutated' test.
    """
    clinical_idea_id = 101
    user_context = UserContext(user_id="test_user", session_rng_seed=123)
    mock_dal = MockDataAccessLayer(concepts_by_idea={clinical_idea_id: sample_concepts})
    presenter = DataPresenter(dal=mock_dal)

    with patch.object(
        mock_dal, "get_all_concepts_for_idea", wraps=mock_dal.get_all_concepts_for_idea
    ) as spy:
        presenter.get_concepts_for_review(clinical_idea_id, user_context)
        spy.assert_called_once_with(clinical_idea_id)


def test_data_package_creation(sample_concepts: List[Concept]):
    """
    Validates that the data package is correctly created with both the
    description and the sanitized, randomized concept list (AL2.4).
    """
    clinical_idea_id = 101
    expected_description = "A study to determine the efficacy of a new drug."
    user_context = UserContext(user_id="test_user", session_rng_seed=123)

    mock_dal = MockDataAccessLayer(
        clinical_idea_descriptions={clinical_idea_id: expected_description},
        concepts_by_idea={clinical_idea_id: sample_concepts},
    )
    presenter = DataPresenter(dal=mock_dal)

    package = presenter.get_concepts_for_review(clinical_idea_id, user_context)

    assert isinstance(package, AdjudicationDataPackage)
    assert package.clinical_idea_description == expected_description
    assert len(package.concepts_for_review) == len(sample_concepts)
    assert isinstance(package.concepts_for_review[0].concept_id, int)


def test_filtering_excludes_sensitive_fields(sample_concepts: List[Concept]):
    """
    CRITICAL (NFR-AL1): Validates that sensitive fields are stripped from the output.
    """
    clinical_idea_id = 1
    user_context = UserContext(user_id="test_user", session_rng_seed=123)
    mock_dal = MockDataAccessLayer(concepts_by_idea={clinical_idea_id: sample_concepts})
    presenter = DataPresenter(dal=mock_dal)

    result = presenter.get_concepts_for_review(clinical_idea_id, user_context)

    for item in result.concepts_for_review:
        assert not hasattr(item, "agreement_level")
        assert not hasattr(item, "contributing_arms")
        assert hasattr(item, "concept_id")
        assert hasattr(item, "name")
        assert hasattr(item, "description")


def test_randomization_shuffles_the_list(sample_concepts: List[Concept]):
    """
    Validates that the list is shuffled and not in its original order (AL2.2).
    """
    clinical_idea_id = 1
    user_context = UserContext(user_id="test_user", session_rng_seed=456)
    mock_dal = MockDataAccessLayer(concepts_by_idea={clinical_idea_id: sample_concepts})
    presenter = DataPresenter(dal=mock_dal)
    original_ids = [c.concept_id for c in sample_concepts]

    result = presenter.get_concepts_for_review(clinical_idea_id, user_context)
    result_ids = [c.concept_id for c in result.concepts_for_review]

    assert len(result_ids) == len(original_ids)
    assert set(result_ids) == set(original_ids)
    assert result_ids != original_ids


def test_seeded_randomization_is_deterministic(sample_concepts: List[Concept]):
    """
    Validates that the same seed produces the same shuffled order every time (AL2.2.1).
    """
    clinical_idea_id = 1
    seed = 789
    mock_dal = MockDataAccessLayer(concepts_by_idea={clinical_idea_id: sample_concepts})
    presenter = DataPresenter(dal=mock_dal)

    context1 = UserContext(user_id="user1", session_rng_seed=seed)
    context2 = UserContext(user_id="user2", session_rng_seed=seed)

    result1 = presenter.get_concepts_for_review(clinical_idea_id, context1)
    result2 = presenter.get_concepts_for_review(clinical_idea_id, context2)

    result1_ids = [c.concept_id for c in result1.concepts_for_review]
    result2_ids = [c.concept_id for c in result2.concepts_for_review]

    assert result1_ids == result2_ids


def test_different_seeds_produce_different_orders(sample_concepts: List[Concept]):
    """
    Validates that different seeds produce different shuffled orders.
    """
    clinical_idea_id = 1
    mock_dal = MockDataAccessLayer(concepts_by_idea={clinical_idea_id: sample_concepts})
    presenter = DataPresenter(dal=mock_dal)

    context1 = UserContext(user_id="user1", session_rng_seed=111)
    context2 = UserContext(user_id="user1", session_rng_seed=999)

    result1 = presenter.get_concepts_for_review(clinical_idea_id, context1)
    result2 = presenter.get_concepts_for_review(clinical_idea_id, context2)

    result1_ids = [c.concept_id for c in result1.concepts_for_review]
    result2_ids = [c.concept_id for c in result2.concepts_for_review]

    assert result1_ids != result2_ids


def test_get_concepts_for_review_with_empty_list():
    """
    Tests the edge case of an empty input list.
    """
    clinical_idea_id = 1
    user_context = UserContext(user_id="test_user", session_rng_seed=123)
    mock_dal = MockDataAccessLayer(concepts_by_idea={clinical_idea_id: []})
    presenter = DataPresenter(dal=mock_dal)

    result = presenter.get_concepts_for_review(clinical_idea_id, user_context)
    assert result.concepts_for_review == []


def test_get_concepts_for_review_with_single_item():
    """
    Tests the edge case of a list with a single concept.
    """
    clinical_idea_id = 1
    user_context = UserContext(user_id="test_user", session_rng_seed=123)
    single_concept = [Concept(100, "Asthma", "Condition", 1, ["ArmX"])]
    mock_dal = MockDataAccessLayer(concepts_by_idea={clinical_idea_id: single_concept})
    presenter = DataPresenter(dal=mock_dal)

    result = presenter.get_concepts_for_review(clinical_idea_id, user_context)

    assert len(result.concepts_for_review) == 1
    assert result.concepts_for_review[0].concept_id == 100
    assert not hasattr(result.concepts_for_review[0], "agreement_level")


@pytest.fixture
def sample_concepts_for_blinding() -> List[Concept]:
    """
    Provides a sample list of Concept objects with sensitive data fields
    specifically for testing the blinding functionality.
    """
    return [
        Concept(
            concept_id=1,
            name="Heart Attack",
            description="Clinical finding of myocardial infarction.",
            agreement_level=3,
            contributing_arms=["ArmA", "ArmB", "ArmC"],
        ),
        Concept(
            concept_id=2,
            name="Diabetes Mellitus",
            description="A group of metabolic disorders.",
            agreement_level=2,
            contributing_arms=["ArmA", "ArmB"],
        ),
    ]


def test_blinding_strips_sensitive_fields(
    sample_concepts_for_blinding: List[Concept],
):
    """
    CRITICAL (NFR-AL1, AL2.1.1): Verifies that the `get_concepts_for_review`
    method strictly removes the `agreement_level` and `contributing_arms`
    fields from the data sent to the user, ensuring compliance with the
    blinding protocol.
    """
    clinical_idea_id = 1
    user_context = UserContext(user_id="test_user", session_rng_seed=123)
    mock_dal = MockDataAccessLayer(
        concepts_by_idea={clinical_idea_id: sample_concepts_for_blinding}
    )
    presenter = DataPresenter(dal=mock_dal)

    # Act
    result = presenter.get_concepts_for_review(clinical_idea_id, user_context)

    # Assert
    assert (
        len(result.concepts_for_review) > 0
    ), "Test setup failed: No concepts returned."

    for concept_view in result.concepts_for_review:
        # 1. Verify it's the correct, sanitized data model
        assert isinstance(
            concept_view, BlindedConceptView
        ), "Returned object is not a BlindedConceptView."

        # 2. CRITICAL: Verify sensitive fields are absent
        assert not hasattr(
            concept_view, "agreement_level"
        ), "Blinding failed: 'agreement_level' was exposed."
        assert not hasattr(
            concept_view, "contributing_arms"
        ), "Blinding failed: 'contributing_arms' were exposed."

        # 3. Verify that non-sensitive fields are present
        assert hasattr(
            concept_view, "concept_id"
        ), "Data integrity failed: 'concept_id' is missing."
        assert hasattr(
            concept_view, "name"
        ), "Data integrity failed: 'name' is missing."
        assert hasattr(
            concept_view, "description"
        ), "Data integrity failed: 'description' is missing."
