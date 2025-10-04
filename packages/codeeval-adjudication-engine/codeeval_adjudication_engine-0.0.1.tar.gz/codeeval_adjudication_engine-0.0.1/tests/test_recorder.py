# Copyright (c) 2025-2026 Gowtham A Rao MD PhD. All Rights Reserved.
#
# This software is proprietary and dual-licensed.
# Licensed under the Prosperity Public License 3.0.0 (the "License").
# A copy of the license is available at https://prosperitylicense.com/versions/3.0.0
# For details, see the LICENSE file.
#
# Commercial use beyond a 30-day trial requires a separate license.
# Contact: rao@ohdsi.org

import unittest
from datetime import datetime, timedelta, timezone
from unittest.mock import create_autospec, patch

import pytest

from codeeval_adjudication_engine.consensus import ConsensusCalculator
from codeeval_adjudication_engine.models import (
    AdjudicationVote,
    AdjudicatorRoster,
    AuthorizationError,
    ClinicalIdeaStatus,
    ConceptConsensusStatus,
    ConceptStatus,
    ConcurrencyConflictError,
    InvalidStateError,
    VoteDecision,
)
from codeeval_adjudication_engine.recorder import VoteRecorder
from codeeval_adjudication_engine.tgs_factory import TGSFactory
from codeeval_adjudication_engine.workflow_manager import WorkflowManager

from .mocks import MockAuditLogger, MockDataAccessLayer

# A constant for the clinical idea ID used in tests
TEST_CLINICAL_IDEA_ID = 101


class TestVoteRecorder(unittest.TestCase):
    """
    Test suite for the VoteRecorder class.
    """

    def setUp(self):
        """Set up a fresh environment for each test."""
        # The WorkflowManager is now the source of truth for the roster.
        self.roster = [
            AdjudicatorRoster(user_id="adj1", is_active=True),
            AdjudicatorRoster(user_id="adj2", is_active=True),
            AdjudicatorRoster(user_id="adj3", is_active=False),  # Inactive
        ]
        self.mock_dal = MockDataAccessLayer(idea_status=ClinicalIdeaStatus.IN_PROGRESS)
        self.consensus_calculator = ConsensusCalculator()
        self.mock_tgs_factory = create_autospec(TGSFactory, instance=True)
        self.mock_audit_logger = MockAuditLogger()
        self.mock_workflow_manager = create_autospec(WorkflowManager, instance=True)

        # Configure the mock workflow manager to return the roster.
        self.mock_workflow_manager.get_roster.return_value = self.roster

        self.vote_recorder = VoteRecorder(
            dal=self.mock_dal,
            consensus_calculator=self.consensus_calculator,
            tgs_factory=self.mock_tgs_factory,
            audit_logger=self.mock_audit_logger,
            workflow_manager=self.mock_workflow_manager,
        )

    def test_submit_vote_success_audits_action(self):
        """Verify that a successful vote submission is correctly audited."""
        self.vote_recorder.submit_vote(
            user_id="adj1",
            concept_id=1,
            decision=VoteDecision.EXCLUDE,
            clinical_idea_id=TEST_CLINICAL_IDEA_ID,
        )
        self.assertEqual(len(self.mock_audit_logger.logged_actions), 1)
        log_entry = self.mock_audit_logger.logged_actions[0]
        self.assertEqual(log_entry["type"], "VOTE")
        self.assertEqual(log_entry["user_id"], "adj1")
        self.assertEqual(log_entry["concept_id"], 1)
        self.assertEqual(log_entry["clinical_idea_id"], TEST_CLINICAL_IDEA_ID)
        self.assertEqual(log_entry["decision"], VoteDecision.EXCLUDE)

    def test_submit_vote_success_consensus_exclude(self):
        self.vote_recorder.submit_vote(
            user_id="adj1",
            concept_id=1,
            decision=VoteDecision.EXCLUDE,
            clinical_idea_id=TEST_CLINICAL_IDEA_ID,
        )
        final_status = self.mock_dal._concept_statuses[1].status
        self.assertEqual(final_status, ConceptConsensusStatus.CONSENSUS_EXCLUDE)
        self.mock_dal.transaction_context.__enter__.assert_called_once()
        self.mock_dal.transaction_context.__exit__.assert_called_once()

    def test_submit_vote_success_consensus_include(self):
        concept_id = 2
        self.vote_recorder.submit_vote(
            user_id="adj1",
            concept_id=concept_id,
            decision=VoteDecision.INCLUDE,
            clinical_idea_id=TEST_CLINICAL_IDEA_ID,
        )
        status_after_1 = self.mock_dal._concept_statuses[concept_id].status
        self.assertEqual(status_after_1, ConceptConsensusStatus.PENDING)
        self.vote_recorder.submit_vote(
            user_id="adj2",
            concept_id=concept_id,
            decision=VoteDecision.INCLUDE,
            clinical_idea_id=TEST_CLINICAL_IDEA_ID,
        )
        status_after_2 = self.mock_dal._concept_statuses[concept_id].status
        self.assertEqual(status_after_2, ConceptConsensusStatus.CONSENSUS_INCLUDE)

    def test_submit_vote_still_pending(self):
        concept_id = 3
        self.vote_recorder.submit_vote(
            user_id="adj1",
            concept_id=concept_id,
            decision=VoteDecision.INCLUDE,
            clinical_idea_id=TEST_CLINICAL_IDEA_ID,
        )
        final_status = self.mock_dal._concept_statuses[concept_id].status
        self.assertEqual(final_status, ConceptConsensusStatus.PENDING)

    def test_adjudicator_changes_vote_updates_consensus(self):
        concept_id = 4
        # Setup: Both adjudicators vote INCLUDE, reaching consensus
        self.mock_dal._votes = [
            AdjudicationVote(
                user_id="adj1",
                concept_id=concept_id,
                decision=VoteDecision.INCLUDE,
                timestamp=datetime.now(timezone.utc),
            ),
            AdjudicationVote(
                user_id="adj2",
                concept_id=concept_id,
                decision=VoteDecision.INCLUDE,
                timestamp=datetime.now(timezone.utc),
            ),
        ]
        self.mock_dal._concept_statuses[concept_id] = ConceptStatus(
            concept_id=concept_id, status=ConceptConsensusStatus.CONSENSUS_INCLUDE
        )

        # Action: adj1 changes their vote to EXCLUDE, breaking consensus
        self.vote_recorder.submit_vote(
            user_id="adj1",
            concept_id=concept_id,
            decision=VoteDecision.EXCLUDE,
            clinical_idea_id=TEST_CLINICAL_IDEA_ID,
        )

        # Assert: The consensus is now EXCLUDE
        status_after_change = self.mock_dal._concept_statuses[concept_id].status
        self.assertEqual(status_after_change, ConceptConsensusStatus.CONSENSUS_EXCLUDE)

    def test_submit_vote_calls_create_vote_for_new_vote_and_adds_timestamp(self):
        """Verify create_vote is called and the vote object includes a timestamp."""
        with patch.object(
            self.mock_dal, "create_vote", wraps=self.mock_dal.create_vote
        ) as spy_create, patch.object(
            self.mock_dal, "update_vote", wraps=self.mock_dal.update_vote
        ) as spy_update:

            self.vote_recorder.submit_vote(
                user_id="adj1",
                concept_id=5,
                decision=VoteDecision.INCLUDE,
                clinical_idea_id=TEST_CLINICAL_IDEA_ID,
            )

            spy_create.assert_called_once()
            spy_update.assert_not_called()

            # Check the created vote object passed to the DAL
            created_vote = spy_create.call_args[0][0]
            self.assertIsInstance(created_vote, AdjudicationVote)
            self.assertIsInstance(created_vote.timestamp, datetime)
            self.assertEqual(created_vote.user_id, "adj1")
            self.assertEqual(created_vote.concept_id, 5)
            self.assertEqual(created_vote.decision, VoteDecision.INCLUDE)

    def test_submit_vote_calls_update_vote_for_existing_vote_and_updates_timestamp(
        self,
    ):
        """Verify update_vote is called and the timestamp is updated."""
        concept_id = 6
        start_time = datetime.now(timezone.utc)
        later_time = start_time + timedelta(seconds=1)

        original_vote = AdjudicationVote(
            user_id="adj1",
            concept_id=concept_id,
            decision=VoteDecision.INCLUDE,
            timestamp=start_time,
        )
        self.mock_dal._votes.append(original_vote)

        with patch.object(
            self.mock_dal, "create_vote", wraps=self.mock_dal.create_vote
        ) as spy_create, patch.object(
            self.mock_dal, "update_vote", wraps=self.mock_dal.update_vote
        ) as spy_update, patch(
            "codeeval_adjudication_engine.recorder.datetime"
        ) as mock_dt:

            mock_dt.now.return_value = later_time

            self.vote_recorder.submit_vote(
                user_id="adj1",
                concept_id=concept_id,
                decision=VoteDecision.EXCLUDE,
                clinical_idea_id=TEST_CLINICAL_IDEA_ID,
            )

            spy_create.assert_not_called()
            spy_update.assert_called_once()

            updated_vote = spy_update.call_args[0][0]
            self.assertIsInstance(updated_vote, AdjudicationVote)
            self.assertIsInstance(updated_vote.timestamp, datetime)
            self.assertGreater(updated_vote.timestamp, original_vote.timestamp)
            self.assertEqual(updated_vote.timestamp, later_time)
            self.assertEqual(updated_vote.decision, VoteDecision.EXCLUDE)

            self.assertIn(updated_vote, self.mock_dal._votes)
            self.assertNotIn(original_vote, self.mock_dal._votes)

    def test_vote_on_finalized_idea_raises_error_from_workflow_manager(self):
        """
        Verify that if the workflow manager raises an InvalidStateError,
        the vote is not processed or audited.
        """
        # Arrange
        self.mock_workflow_manager.start_adjudication.side_effect = InvalidStateError(
            "Idea is finalized"
        )

        # Act & Assert
        with self.assertRaises(InvalidStateError):
            self.vote_recorder.submit_vote(
                user_id="adj1",
                concept_id=7,
                decision=VoteDecision.INCLUDE,
                clinical_idea_id=TEST_CLINICAL_IDEA_ID,
            )
        self.assertEqual(len(self.mock_audit_logger.logged_actions), 0)

    def test_vote_from_inactive_adjudicator_raises_error_and_does_not_audit(self):
        """Verify voting from an inactive user raises an error and is not audited."""
        with self.assertRaises(AuthorizationError):
            self.vote_recorder.submit_vote(
                user_id="adj3",
                concept_id=8,
                decision=VoteDecision.INCLUDE,
                clinical_idea_id=TEST_CLINICAL_IDEA_ID,
            )
        self.assertEqual(len(self.mock_audit_logger.logged_actions), 0)

    def test_vote_from_unassigned_adjudicator_raises_error_and_does_not_audit(self):
        """Verify voting from an unassigned user raises an error and is not audited."""
        with self.assertRaises(AuthorizationError):
            self.vote_recorder.submit_vote(
                user_id="adj4_imposter",
                concept_id=9,
                decision=VoteDecision.INCLUDE,
                clinical_idea_id=TEST_CLINICAL_IDEA_ID,
            )
        self.assertEqual(len(self.mock_audit_logger.logged_actions), 0)

    def test_concurrency_conflict_error_is_raised(self):
        """Verify a concurrency error still audits but does not save the vote."""
        self.mock_dal.get_concept_status_for_update = create_autospec(
            self.mock_dal.get_concept_status_for_update,
            side_effect=ConcurrencyConflictError("Failed to acquire lock"),
        )

        # Re-initialize with the mocked DAL method
        self.vote_recorder = VoteRecorder(
            dal=self.mock_dal,
            consensus_calculator=self.consensus_calculator,
            tgs_factory=self.mock_tgs_factory,
            audit_logger=self.mock_audit_logger,
            workflow_manager=self.mock_workflow_manager,
        )

        with self.assertRaises(ConcurrencyConflictError):
            self.vote_recorder.submit_vote(
                user_id="adj1",
                concept_id=10,
                decision=VoteDecision.INCLUDE,
                clinical_idea_id=TEST_CLINICAL_IDEA_ID,
            )

        # The audit should happen BEFORE the transaction that fails
        self.assertEqual(len(self.mock_audit_logger.logged_actions), 1)

        # The transaction should be attempted and failed
        self.mock_dal.transaction_context.__enter__.assert_called_once()
        self.mock_dal.transaction_context.__exit__.assert_called_once()

        # No vote should have been persisted
        self.assertEqual(len(self.mock_dal._votes), 0)
        self.mock_tgs_factory.check_and_finalize.assert_not_called()

    @pytest.mark.xfail(
        reason="BUG: Transactional rollback is not working correctly.", strict=True
    )
    def test_submit_vote_rolls_back_on_downstream_error(self):
        """
        Verify that if a downstream operation like consensus calculation fails,
        the vote creation is rolled back, ensuring atomicity.
        """
        # Arrange: Mock the consensus calculator to fail.
        error_message = "Consensus calculation failed!"
        # Refactor to avoid long line issue.
        calc_consensus_spec = create_autospec(
            self.consensus_calculator.calculate_consensus,
            side_effect=ValueError(error_message),
        )
        self.consensus_calculator.calculate_consensus = calc_consensus_spec

        # Re-initialize the recorder with the faulty dependency
        self.vote_recorder = VoteRecorder(
            dal=self.mock_dal,
            consensus_calculator=self.consensus_calculator,
            tgs_factory=self.mock_tgs_factory,
            audit_logger=self.mock_audit_logger,
            workflow_manager=self.mock_workflow_manager,
        )

        # Act & Assert: The exception from the mocked calculator should propagate
        with self.assertRaisesRegex(ValueError, error_message):
            self.vote_recorder.submit_vote(
                user_id="adj1",
                concept_id=1,
                decision=VoteDecision.INCLUDE,
                clinical_idea_id=TEST_CLINICAL_IDEA_ID,
            )

        # Assert: The transaction was started and exited (due to the exception)
        self.mock_dal.transaction_context.__enter__.assert_called_once()
        self.mock_dal.transaction_context.__exit__.assert_called_once()

        # CRITICAL: Assert that no vote was persisted in the DAL.
        # This confirms the rollback behavior of the transaction.
        self.assertEqual(len(self.mock_dal._votes), 0)

        # The audit log should still exist, as it happens *before* the transaction
        self.assertEqual(len(self.mock_audit_logger.logged_actions), 1)

        # The finalization check should not be reached
        self.mock_tgs_factory.check_and_finalize.assert_not_called()

    def test_tgs_factory_is_called_after_vote(self):
        self.vote_recorder.submit_vote(
            user_id="adj1",
            concept_id=11,
            decision=VoteDecision.INCLUDE,
            clinical_idea_id=TEST_CLINICAL_IDEA_ID,
        )
        # Assign to a shorter name to avoid line-length issues
        check_and_finalize_mock = self.mock_tgs_factory.check_and_finalize
        check_and_finalize_mock.assert_called_once_with(TEST_CLINICAL_IDEA_ID)

    def test_submit_vote_always_calls_start_adjudication(self):
        """
        Verify that submitting a vote always calls the start_adjudication method
        on the workflow manager to ensure the state is correct.
        """
        # Act
        self.vote_recorder.submit_vote(
            user_id="adj1",
            concept_id=1,
            decision=VoteDecision.INCLUDE,
            clinical_idea_id=TEST_CLINICAL_IDEA_ID,
        )

        # Assert
        self.mock_workflow_manager.start_adjudication.assert_called_once_with(
            TEST_CLINICAL_IDEA_ID
        )


if __name__ == "__main__":
    unittest.main()
