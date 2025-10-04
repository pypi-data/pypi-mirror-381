from unittest.mock import MagicMock

import pytest

from src.codeeval_adjudication_engine.models import (
    AdjudicatorRoster,
    ClinicalIdeaStatus,
    InvalidStateError,
)
from src.codeeval_adjudication_engine.workflow_manager import WorkflowManager
from tests.mocks import MockDataAccessLayer


@pytest.fixture
def mock_dal():
    """Pytest fixture for a mock DataAccessLayer."""
    return MockDataAccessLayer()


@pytest.fixture
def workflow_manager(mock_dal):
    """Pytest fixture for a WorkflowManager instance."""
    return WorkflowManager(dal=mock_dal)


def test_get_roster_calls_dal_correctly(workflow_manager, mock_dal):
    """
    Tests that get_roster correctly calls the DAL's get_active_roster method.
    """
    # Arrange
    clinical_idea_id = 1
    expected_roster = [AdjudicatorRoster(user_id="adjudicator1")]
    mock_dal.get_active_roster = MagicMock(return_value=expected_roster)

    # Act
    roster = workflow_manager.get_roster(clinical_idea_id)

    # Assert
    mock_dal.get_active_roster.assert_called_once_with(clinical_idea_id)
    assert roster == expected_roster


def test_modify_roster_deactivates_and_invalidates_votes(workflow_manager, mock_dal):
    """
    Tests that modify_roster calls both modify_roster_status and invalidate_votes
    when deactivating an adjudicator.
    """
    # Arrange
    clinical_idea_id = 1
    user_id_to_modify = "adjudicator_to_remove"
    mock_dal.modify_roster_status = MagicMock()
    mock_dal.invalidate_votes = MagicMock()

    # Act
    workflow_manager.modify_roster(
        clinical_idea_id, user_id_to_modify, new_active_status=False
    )

    # Assert
    mock_dal.modify_roster_status.assert_called_once_with(
        clinical_idea_id, user_id_to_modify, False
    )
    mock_dal.invalidate_votes.assert_called_once_with(
        clinical_idea_id, user_id_to_modify
    )


def test_modify_roster_activates_without_invalidating_votes(workflow_manager, mock_dal):
    """
    Tests that modify_roster only calls modify_roster_status and not
    invalidate_votes when activating an adjudicator.
    """
    # Arrange
    clinical_idea_id = 1
    user_id_to_modify = "adjudicator_to_add"
    mock_dal.modify_roster_status = MagicMock()
    mock_dal.invalidate_votes = MagicMock()

    # Act
    workflow_manager.modify_roster(
        clinical_idea_id, user_id_to_modify, new_active_status=True
    )

    # Assert
    mock_dal.modify_roster_status.assert_called_once_with(
        clinical_idea_id, user_id_to_modify, True
    )
    mock_dal.invalidate_votes.assert_not_called()


def test_start_adjudication_transitions_from_pending(workflow_manager, mock_dal):
    """
    Tests that start_adjudication correctly transitions a PENDING idea to
    IN_PROGRESS.
    """
    # Arrange
    clinical_idea_id = 1
    mock_dal.get_clinical_idea_status = MagicMock(
        return_value=ClinicalIdeaStatus.PENDING
    )
    mock_dal.update_clinical_idea_status = MagicMock()

    # Act
    workflow_manager.start_adjudication(clinical_idea_id)

    # Assert
    mock_dal.get_clinical_idea_status.assert_called_once_with(clinical_idea_id)
    mock_dal.update_clinical_idea_status.assert_called_once_with(
        clinical_idea_id, ClinicalIdeaStatus.IN_PROGRESS
    )


def test_start_adjudication_is_idempotent_for_in_progress(workflow_manager, mock_dal):
    """
    Tests that start_adjudication makes no changes if the idea is already
    IN_PROGRESS.
    """
    # Arrange
    clinical_idea_id = 1
    mock_dal.get_clinical_idea_status = MagicMock(
        return_value=ClinicalIdeaStatus.IN_PROGRESS
    )
    mock_dal.update_clinical_idea_status = MagicMock()

    # Act
    workflow_manager.start_adjudication(clinical_idea_id)

    # Assert
    mock_dal.get_clinical_idea_status.assert_called_once_with(clinical_idea_id)
    mock_dal.update_clinical_idea_status.assert_not_called()


def test_start_adjudication_raises_error_for_finalized(workflow_manager, mock_dal):
    """
    Tests that start_adjudication raises an InvalidStateError if the idea is
    already FINALIZED.
    """
    # Arrange
    clinical_idea_id = 1
    mock_dal.get_clinical_idea_status = MagicMock(
        return_value=ClinicalIdeaStatus.FINALIZED
    )

    # Act & Assert
    with pytest.raises(InvalidStateError):
        workflow_manager.start_adjudication(clinical_idea_id)


# --- Tests for centralized state transition logic ---


@pytest.mark.parametrize(
    "current_status, new_status",
    [
        (ClinicalIdeaStatus.PENDING, ClinicalIdeaStatus.IN_PROGRESS),
        (ClinicalIdeaStatus.IN_PROGRESS, ClinicalIdeaStatus.FINALIZED),
    ],
)
def test_update_status_valid_transitions(
    workflow_manager, mock_dal, current_status, new_status
):
    """
    Tests that valid state transitions are executed correctly.
    """
    # Arrange
    clinical_idea_id = 1
    mock_dal.get_clinical_idea_status = MagicMock(return_value=current_status)
    mock_dal.update_clinical_idea_status = MagicMock()

    # Act
    workflow_manager.update_clinical_idea_status(clinical_idea_id, new_status)

    # Assert
    mock_dal.update_clinical_idea_status.assert_called_once_with(
        clinical_idea_id, new_status
    )


@pytest.mark.parametrize(
    "current_status, new_status",
    [
        (ClinicalIdeaStatus.PENDING, ClinicalIdeaStatus.FINALIZED),
        (ClinicalIdeaStatus.IN_PROGRESS, ClinicalIdeaStatus.PENDING),
        (ClinicalIdeaStatus.FINALIZED, ClinicalIdeaStatus.IN_PROGRESS),
        (ClinicalIdeaStatus.FINALIZED, ClinicalIdeaStatus.PENDING),
    ],
)
def test_update_status_invalid_transitions_raise_error(
    workflow_manager, mock_dal, current_status, new_status
):
    """
    Tests that InvalidStateError is raised for invalid state transitions.
    """
    # Arrange
    clinical_idea_id = 1
    mock_dal.get_clinical_idea_status = MagicMock(return_value=current_status)

    # Act & Assert
    with pytest.raises(InvalidStateError) as excinfo:
        workflow_manager.update_clinical_idea_status(clinical_idea_id, new_status)
    assert f"Invalid state transition for clinical idea {clinical_idea_id}" in str(
        excinfo.value
    )


@pytest.mark.parametrize(
    "status",
    [
        ClinicalIdeaStatus.PENDING,
        ClinicalIdeaStatus.IN_PROGRESS,
        ClinicalIdeaStatus.FINALIZED,
    ],
)
def test_update_status_is_idempotent(workflow_manager, mock_dal, status):
    """
    Tests that no action is taken if the new status is the same as the current one.
    """
    # Arrange
    clinical_idea_id = 1
    mock_dal.get_clinical_idea_status = MagicMock(return_value=status)
    mock_dal.update_clinical_idea_status = MagicMock()

    # Act
    workflow_manager.update_clinical_idea_status(clinical_idea_id, status)

    # Assert
    mock_dal.update_clinical_idea_status.assert_not_called()


# --- Tests for specific methods mentioned in audit ---


@pytest.mark.parametrize(
    "user_id, is_in_roster, is_active_in_roster, expected",
    [
        ("authorized_user", True, True, True),
        ("inactive_user", True, False, False),
        ("unlisted_user", False, False, False),
    ],
)
def test_is_adjudicator_authorized(
    workflow_manager, mock_dal, user_id, is_in_roster, is_active_in_roster, expected
):
    """
    Tests the is_adjudicator_authorized method for various scenarios.
    FRD AL1.1
    """
    # Arrange
    roster = []
    if is_in_roster:
        roster.append(AdjudicatorRoster(user_id=user_id, is_active=is_active_in_roster))
    mock_dal.get_active_roster = MagicMock(return_value=roster)
    clinical_idea_id = 1

    # Act
    is_authorized = workflow_manager.is_adjudicator_authorized(
        user_id, clinical_idea_id
    )

    # Assert
    assert is_authorized is expected


def test_update_concept_status_success(workflow_manager, mock_dal):
    """
    Tests that update_concept_status successfully calls the DAL when the
    clinical idea is not finalized.
    FRD AL1.3
    """
    # Arrange
    clinical_idea_id = 1
    concept_id = 101
    new_status = "CONSENSUS_INCLUDE"
    mock_dal.get_clinical_idea_status = MagicMock(
        return_value=ClinicalIdeaStatus.IN_PROGRESS
    )
    mock_dal.update_concept_status = MagicMock()

    # Act
    workflow_manager.update_concept_status(clinical_idea_id, concept_id, new_status)

    # Assert
    mock_dal.get_clinical_idea_status.assert_called_once_with(clinical_idea_id)
    mock_dal.update_concept_status.assert_called_once_with(concept_id, new_status)


def test_update_concept_status_raises_error_for_finalized_idea(
    workflow_manager, mock_dal
):
    """
    Tests that update_concept_status raises an InvalidStateError if the
    clinical idea is already FINALIZED.
    FRD AL1.3
    """
    # Arrange
    clinical_idea_id = 1
    concept_id = 101
    new_status = "CONSENSUS_INCLUDE"
    mock_dal.get_clinical_idea_status = MagicMock(
        return_value=ClinicalIdeaStatus.FINALIZED
    )
    mock_dal.update_concept_status = MagicMock()

    # Act & Assert
    with pytest.raises(InvalidStateError) as excinfo:
        workflow_manager.update_concept_status(clinical_idea_id, concept_id, new_status)
    assert f"clinical idea {clinical_idea_id} is already finalized" in str(
        excinfo.value
    )
    mock_dal.update_concept_status.assert_not_called()
