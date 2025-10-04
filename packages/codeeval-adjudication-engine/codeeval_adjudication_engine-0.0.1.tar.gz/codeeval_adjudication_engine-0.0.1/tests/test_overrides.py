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
from unittest.mock import call

import pytest

from codeeval_adjudication_engine.consensus import ConsensusCalculator
from codeeval_adjudication_engine.models import (
    AdjudicationVote,
    AdjudicatorRoster,
    AuthorizationError,
    ClinicalIdeaStatus,
    ConceptConsensusStatus,
    ConceptStatus,
    InvalidStateError,
    UserContext,
    VoteDecision,
)
from codeeval_adjudication_engine.overrides import OverrideManager
from codeeval_adjudication_engine.tgs_factory import TGSFactory
from tests.mocks import (
    MockAuditLogger,
    MockDataAccessLayer,
    MockTGSFinalizationNotifier,
    MockWorkflowManager,
)


# --- Fixtures for common test objects ---
@pytest.fixture
def mock_dal() -> MockDataAccessLayer:
    """Provides a fresh instance of the centralized MockDataAccessLayer."""
    return MockDataAccessLayer()


@pytest.fixture
def mock_workflow_manager(mock_dal: MockDataAccessLayer) -> MockWorkflowManager:
    """Provides a mock WorkflowManager that uses the shared DAL."""
    return MockWorkflowManager(mock_dal)


@pytest.fixture
def mock_tgs_notifier() -> MockTGSFinalizationNotifier:
    """Provides a mock TGSFinalizationNotifier."""
    return MockTGSFinalizationNotifier()


@pytest.fixture
def mock_audit_logger() -> MockAuditLogger:
    """Provides a fresh instance of the centralized MockAuditLogger."""
    return MockAuditLogger()


@pytest.fixture
def session_lead_context() -> UserContext:
    """Provides a UserContext for a Session Lead."""
    return UserContext(
        user_id="lead_user_001", session_rng_seed=123, roles=["Session Lead"]
    )


@pytest.fixture
def regular_user_context() -> UserContext:
    """Provides a UserContext for a regular Adjudicator."""
    return UserContext(
        user_id="regular_user_002", session_rng_seed=456, roles=["Adjudicator"]
    )


# --- Test Cases ---


def test_modify_adjudicator_roster_deactivation_success(
    session_lead_context,
    mock_dal,
    mock_tgs_notifier,
    mock_workflow_manager,
    mock_audit_logger,
):
    """
    Tests that OverrideManager correctly uses WorkflowManager to deactivate
    an adjudicator and that consensus is recalculated.
    FRD AL7.1, AL7.3, AL7.4, AL7.5
    """
    # Arrange
    clinical_idea_id = 1
    user_to_deactivate = "adj_2"
    mock_dal._roster = [
        AdjudicatorRoster("adj_1"),
        AdjudicatorRoster(user_to_deactivate),
    ]
    mock_dal._votes = [
        AdjudicationVote(
            user_to_deactivate,
            101,
            VoteDecision.INCLUDE,
            timestamp=datetime.now(timezone.utc),
        )
    ]
    mock_dal._concept_statuses = {
        101: ConceptStatus(101, ConceptConsensusStatus.PENDING),
        102: ConceptStatus(102, ConceptConsensusStatus.PENDING),
    }
    mock_dal._idea_status = ClinicalIdeaStatus.IN_PROGRESS

    tgs_factory = TGSFactory(
        mock_dal, mock_tgs_notifier, mock_audit_logger, mock_workflow_manager
    )
    consensus_calculator = ConsensusCalculator()
    manager = OverrideManager(
        mock_dal,
        consensus_calculator,
        tgs_factory,
        mock_audit_logger,
        mock_workflow_manager,
    )

    # Act
    manager.modify_adjudicator_roster(
        clinical_idea_id, user_to_deactivate, False, session_lead_context
    )

    # Assert
    mock_workflow_manager.modify_roster.assert_called_once_with(
        clinical_idea_id, user_to_deactivate, False
    )
    mock_workflow_manager.get_roster.assert_called_once_with(clinical_idea_id)
    assert len(mock_audit_logger.logged_actions) == 1
    assert (
        mock_audit_logger.logged_actions[0]["affected_adjudicator_id"]
        == user_to_deactivate
    )
    assert (
        mock_dal.get_clinical_idea_status(clinical_idea_id)
        == ClinicalIdeaStatus.IN_PROGRESS
    )
    assert len(mock_tgs_notifier.notified_ideas) == 0


def test_auditing_occurs_on_roster_modification(
    session_lead_context,
    mock_dal,
    mock_tgs_notifier,
    mock_workflow_manager,
    mock_audit_logger,
):
    """
    Verifies that modifying a roster correctly logs the action to the database.
    FRD AL7.6
    """
    # Arrange
    clinical_idea_id = 1
    user_to_modify = "adj_2"
    mock_dal._idea_status = ClinicalIdeaStatus.IN_PROGRESS
    mock_dal._concept_statuses = {
        999: ConceptStatus(999, ConceptConsensusStatus.PENDING)
    }

    tgs_factory = TGSFactory(
        mock_dal, mock_tgs_notifier, mock_audit_logger, mock_workflow_manager
    )
    consensus_calculator = ConsensusCalculator()
    manager = OverrideManager(
        mock_dal,
        consensus_calculator,
        tgs_factory,
        mock_audit_logger,
        mock_workflow_manager,
    )

    # Act
    manager.modify_adjudicator_roster(
        clinical_idea_id, user_to_modify, False, session_lead_context
    )
    manager.modify_adjudicator_roster(
        clinical_idea_id, user_to_modify, True, session_lead_context
    )

    # Assert
    assert len(mock_audit_logger.logged_actions) == 2
    mock_workflow_manager.modify_roster.assert_has_calls(
        [
            call(clinical_idea_id, user_to_modify, False),
            call(clinical_idea_id, user_to_modify, True),
        ]
    )
    assert mock_audit_logger.logged_actions[0]["action"] == "DEACTIVATE"
    assert mock_audit_logger.logged_actions[1]["action"] == "ACTIVATE"


def test_authorization_failure(
    regular_user_context,
    mock_dal,
    mock_tgs_notifier,
    mock_workflow_manager,
    mock_audit_logger,
):
    """
    Tests that non-Session Leads cannot modify the roster.
    FRD AL7.2.1
    """
    tgs_factory = TGSFactory(
        mock_dal, mock_tgs_notifier, mock_audit_logger, mock_workflow_manager
    )
    consensus_calculator = ConsensusCalculator()
    manager = OverrideManager(
        mock_dal,
        consensus_calculator,
        tgs_factory,
        mock_audit_logger,
        mock_workflow_manager,
    )

    with pytest.raises(AuthorizationError):
        manager.modify_adjudicator_roster(1, "user_1", False, regular_user_context)

    assert len(mock_audit_logger.logged_actions) == 0
    mock_workflow_manager.modify_roster.assert_not_called()


def test_invalid_state_failure(
    session_lead_context,
    mock_dal,
    mock_tgs_notifier,
    mock_workflow_manager,
    mock_audit_logger,
):
    """
    Tests that the roster cannot be modified for a FINALIZED clinical idea.
    FRD AL7.2.2
    """
    mock_dal._idea_status = ClinicalIdeaStatus.FINALIZED
    tgs_factory = TGSFactory(
        mock_dal, mock_tgs_notifier, mock_audit_logger, mock_workflow_manager
    )
    consensus_calculator = ConsensusCalculator()
    manager = OverrideManager(
        mock_dal,
        consensus_calculator,
        tgs_factory,
        mock_audit_logger,
        mock_workflow_manager,
    )

    with pytest.raises(InvalidStateError):
        manager.modify_adjudicator_roster(1, "user_1", False, session_lead_context)

    assert len(mock_audit_logger.logged_actions) == 0
    mock_workflow_manager.modify_roster.assert_not_called()


def test_consensus_changes_after_deactivating_blocking_voter(
    session_lead_context,
    mock_dal,
    mock_tgs_notifier,
    mock_workflow_manager,
    mock_audit_logger,
):
    """
    A complex scenario showing that consensus is recalculated correctly when an
    adjudicator with a deciding 'Exclude' vote is removed.
    """
    # Arrange
    clinical_idea_id = 1
    concept_id = 101
    user_to_deactivate = "adj_blocking"
    mock_dal._roster = [
        AdjudicatorRoster("adj_1"),
        AdjudicatorRoster(user_to_deactivate),
        AdjudicatorRoster("adj_3"),
    ]
    mock_dal._votes = [
        AdjudicationVote(
            "adj_1",
            concept_id,
            VoteDecision.INCLUDE,
            timestamp=datetime.now(timezone.utc),
        ),
        AdjudicationVote(
            user_to_deactivate,
            concept_id,
            VoteDecision.EXCLUDE,
            timestamp=datetime.now(timezone.utc),
        ),
        AdjudicationVote(
            "adj_3",
            concept_id,
            VoteDecision.INCLUDE,
            timestamp=datetime.now(timezone.utc),
        ),
    ]
    mock_dal._concept_statuses = {
        concept_id: ConceptStatus(concept_id, ConceptConsensusStatus.CONSENSUS_EXCLUDE)
    }
    mock_dal._idea_status = ClinicalIdeaStatus.IN_PROGRESS

    tgs_factory = TGSFactory(
        mock_dal, mock_tgs_notifier, mock_audit_logger, mock_workflow_manager
    )
    consensus_calculator = ConsensusCalculator()
    manager = OverrideManager(
        mock_dal,
        consensus_calculator,
        tgs_factory,
        mock_audit_logger,
        mock_workflow_manager,
    )

    # Act
    manager.modify_adjudicator_roster(
        clinical_idea_id, user_to_deactivate, False, session_lead_context
    )

    # Assert
    final_status = mock_dal._concept_statuses[concept_id].status
    assert final_status == ConceptConsensusStatus.CONSENSUS_INCLUDE
    # An override action and a TGS finalization action should be logged.
    assert len(mock_audit_logger.logged_actions) == 2
    assert (
        mock_audit_logger.logged_actions[0]["affected_adjudicator_id"]
        == user_to_deactivate
    )


def test_tgs_is_finalized_after_roster_change_resolves_last_concept(
    session_lead_context,
    mock_dal,
    mock_tgs_notifier,
    mock_workflow_manager,
    mock_audit_logger,
):
    """
    Tests that the TGSFactory finalizes the idea when a roster modification
    resolves the final pending concept.
    """
    # Arrange
    clinical_idea_id = 1
    concept_id = 101
    user_to_deactivate = "adj_blocking"
    mock_dal._roster = [
        AdjudicatorRoster("adj_1"),
        AdjudicatorRoster(user_to_deactivate),
    ]
    mock_dal._votes = [
        AdjudicationVote(
            "adj_1",
            concept_id,
            VoteDecision.INCLUDE,
            timestamp=datetime.now(timezone.utc),
        ),
        AdjudicationVote(
            user_to_deactivate,
            concept_id,
            VoteDecision.EXCLUDE,
            timestamp=datetime.now(timezone.utc),
        ),
    ]
    mock_dal._concept_statuses = {
        concept_id: ConceptStatus(concept_id, ConceptConsensusStatus.PENDING)
    }
    mock_dal._idea_status = ClinicalIdeaStatus.IN_PROGRESS

    tgs_factory = TGSFactory(
        mock_dal, mock_tgs_notifier, mock_audit_logger, mock_workflow_manager
    )
    consensus_calculator = ConsensusCalculator()
    manager = OverrideManager(
        mock_dal,
        consensus_calculator,
        tgs_factory,
        mock_audit_logger,
        mock_workflow_manager,
    )

    # Act
    manager.modify_adjudicator_roster(
        clinical_idea_id, user_to_deactivate, False, session_lead_context
    )

    # Assert
    final_status = mock_dal._concept_statuses[concept_id].status
    assert final_status == ConceptConsensusStatus.CONSENSUS_INCLUDE
    assert (
        mock_dal.get_clinical_idea_status(clinical_idea_id)
        == ClinicalIdeaStatus.FINALIZED
    )
    assert mock_tgs_notifier.notified_ideas == [clinical_idea_id]
