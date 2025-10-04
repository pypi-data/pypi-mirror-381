# Copyright (c) 2025-2026 Gowtham A Rao MD PhD. All Rights Reserved.
#
# This software is proprietary and dual-licensed.
# Licensed under the Prosperity Public License 3.0.0 (the "License").
# A copy of the license is available at https://prosperitylicense.com/versions/3.0.0
# For details, see the LICENSE file.
#
# Commercial use beyond a 30-day trial requires a separate license.
# Contact: rao@ohdsi.org

import pytest

from codeeval_adjudication_engine.models import (
    ClinicalIdeaStatus,
    ConceptConsensusStatus,
    ConceptStatus,
)
from codeeval_adjudication_engine.tgs_factory import TGSFactory
from tests.mocks import (
    MockAuditLogger,
    MockDataAccessLayer,
    MockTGSFinalizationNotifier,
    MockWorkflowManager,
)

# A test clinical idea ID to use across tests for consistency.
TEST_CLINICAL_IDEA_ID = 456


@pytest.fixture
def mock_dal() -> MockDataAccessLayer:
    """Provides a fresh, shared instance of the MockDataAccessLayer."""
    return MockDataAccessLayer()


@pytest.fixture
def mock_notifier() -> MockTGSFinalizationNotifier:
    """Provides a fresh instance of the MockTGSFinalizationNotifier."""
    return MockTGSFinalizationNotifier()


@pytest.fixture
def mock_audit_logger() -> MockAuditLogger:
    """Provides a fresh instance of the MockAuditLogger."""
    return MockAuditLogger()


@pytest.fixture
def mock_workflow_manager(mock_dal: MockDataAccessLayer) -> MockWorkflowManager:
    """Provides a MockWorkflowManager that shares the test's DAL instance."""
    return MockWorkflowManager(mock_dal)


def test_tgs_factory_finalizes_when_all_concepts_resolved(
    mock_dal: MockDataAccessLayer,
    mock_notifier: MockTGSFinalizationNotifier,
    mock_audit_logger: MockAuditLogger,
    mock_workflow_manager: MockWorkflowManager,
):
    """
    Verifies FRD AL5.1 & AL5.2 - TGS is finalized when all concepts are resolved.
    """
    # Arrange
    mock_dal._concept_statuses = {
        101: ConceptStatus(
            concept_id=101, status=ConceptConsensusStatus.CONSENSUS_INCLUDE
        ),
        102: ConceptStatus(
            concept_id=102, status=ConceptConsensusStatus.CONSENSUS_EXCLUDE
        ),
        103: ConceptStatus(
            concept_id=103, status=ConceptConsensusStatus.CONSENSUS_INCLUDE
        ),
    }
    mock_dal._intersection_concepts = [901, 902]
    mock_dal._idea_status = ClinicalIdeaStatus.IN_PROGRESS
    factory = TGSFactory(
        dal=mock_dal,
        notifier=mock_notifier,
        audit_logger=mock_audit_logger,
        workflow_manager=mock_workflow_manager,
    )

    # Act
    factory.check_and_finalize(TEST_CLINICAL_IDEA_ID)

    # Assert
    assert mock_dal.saved_tgs is not None
    assert mock_dal.saved_tgs.clinical_idea_id == TEST_CLINICAL_IDEA_ID
    assert mock_dal.saved_tgs.concept_ids == [101, 103, 901, 902]
    mock_workflow_manager.update_clinical_idea_status.assert_called_once_with(
        TEST_CLINICAL_IDEA_ID, ClinicalIdeaStatus.FINALIZED
    )


def test_tgs_factory_does_not_finalize_if_concepts_pending(
    mock_dal: MockDataAccessLayer,
    mock_notifier: MockTGSFinalizationNotifier,
    mock_audit_logger: MockAuditLogger,
    mock_workflow_manager: MockWorkflowManager,
):
    """
    Verifies FRD AL5.1 - TGS is not finalized if any concept is still PENDING.
    """
    # Arrange
    mock_dal._concept_statuses = {
        101: ConceptStatus(
            concept_id=101, status=ConceptConsensusStatus.CONSENSUS_INCLUDE
        ),
        102: ConceptStatus(concept_id=102, status=ConceptConsensusStatus.PENDING),
    }
    mock_dal._idea_status = ClinicalIdeaStatus.IN_PROGRESS
    factory = TGSFactory(
        dal=mock_dal,
        notifier=mock_notifier,
        audit_logger=mock_audit_logger,
        workflow_manager=mock_workflow_manager,
    )

    # Act
    factory.check_and_finalize(TEST_CLINICAL_IDEA_ID)

    # Assert
    assert mock_dal.saved_tgs is None
    mock_workflow_manager.update_clinical_idea_status.assert_not_called()


def test_tgs_factory_finalizes_empty_clinical_idea(
    mock_dal: MockDataAccessLayer,
    mock_notifier: MockTGSFinalizationNotifier,
    mock_audit_logger: MockAuditLogger,
    mock_workflow_manager: MockWorkflowManager,
):
    """
    Verifies edge case: An idea with no "Delta" concepts is immediately finalizable.
    """
    # Arrange
    mock_dal._concept_statuses = {}
    mock_dal._intersection_concepts = [901]
    mock_dal._idea_status = ClinicalIdeaStatus.IN_PROGRESS
    factory = TGSFactory(
        dal=mock_dal,
        notifier=mock_notifier,
        audit_logger=mock_audit_logger,
        workflow_manager=mock_workflow_manager,
    )

    # Act
    factory.check_and_finalize(TEST_CLINICAL_IDEA_ID)

    # Assert
    assert mock_dal.saved_tgs is not None
    assert mock_dal.saved_tgs.concept_ids == [901]
    mock_workflow_manager.update_clinical_idea_status.assert_called_once_with(
        TEST_CLINICAL_IDEA_ID, ClinicalIdeaStatus.FINALIZED
    )


def test_tgs_factory_notifies_downstream_system_on_finalization(
    mock_dal: MockDataAccessLayer,
    mock_notifier: MockTGSFinalizationNotifier,
    mock_audit_logger: MockAuditLogger,
    mock_workflow_manager: MockWorkflowManager,
):
    """
    Verifies FRD AL5.4 - A notification must be sent upon TGS finalization.
    """
    # Arrange
    mock_dal._concept_statuses = {
        101: ConceptStatus(
            concept_id=101, status=ConceptConsensusStatus.CONSENSUS_INCLUDE
        )
    }
    mock_dal._idea_status = ClinicalIdeaStatus.IN_PROGRESS
    factory = TGSFactory(
        dal=mock_dal,
        notifier=mock_notifier,
        audit_logger=mock_audit_logger,
        workflow_manager=mock_workflow_manager,
    )

    # Act
    factory.check_and_finalize(TEST_CLINICAL_IDEA_ID)

    # Assert
    assert mock_notifier.notified_ideas == [TEST_CLINICAL_IDEA_ID]


def test_tgs_factory_does_not_notify_if_not_finalized(
    mock_dal: MockDataAccessLayer,
    mock_notifier: MockTGSFinalizationNotifier,
    mock_audit_logger: MockAuditLogger,
    mock_workflow_manager: MockWorkflowManager,
):
    """
    Verifies FRD AL5.4 - A notification must NOT be sent if TGS is not finalized.
    """
    # Arrange
    mock_dal._concept_statuses = {
        101: ConceptStatus(concept_id=101, status=ConceptConsensusStatus.PENDING)
    }
    factory = TGSFactory(
        dal=mock_dal,
        notifier=mock_notifier,
        audit_logger=mock_audit_logger,
        workflow_manager=mock_workflow_manager,
    )

    # Act
    factory.check_and_finalize(TEST_CLINICAL_IDEA_ID)

    # Assert
    assert not mock_notifier.notified_ideas


def test_tgs_factory_audits_finalization_event(
    mock_dal: MockDataAccessLayer,
    mock_notifier: MockTGSFinalizationNotifier,
    mock_audit_logger: MockAuditLogger,
    mock_workflow_manager: MockWorkflowManager,
):
    """
    Verifies that the TGSFactory logs an audit event upon successful finalization.
    """
    # Arrange
    mock_dal._concept_statuses = {
        101: ConceptStatus(
            concept_id=101, status=ConceptConsensusStatus.CONSENSUS_INCLUDE
        ),
    }
    mock_dal._intersection_concepts = [901]
    mock_dal._idea_status = ClinicalIdeaStatus.IN_PROGRESS
    factory = TGSFactory(
        dal=mock_dal,
        notifier=mock_notifier,
        audit_logger=mock_audit_logger,
        workflow_manager=mock_workflow_manager,
    )
    expected_final_ids = [101, 901]

    # Act
    factory.check_and_finalize(TEST_CLINICAL_IDEA_ID)

    # Assert
    assert len(mock_audit_logger.logged_actions) == 1
    log_entry = mock_audit_logger.logged_actions[0]
    assert log_entry["type"] == "TGS_FINALIZATION"
    assert log_entry["clinical_idea_id"] == TEST_CLINICAL_IDEA_ID
    assert log_entry["final_tgs_concept_ids"] == expected_final_ids
