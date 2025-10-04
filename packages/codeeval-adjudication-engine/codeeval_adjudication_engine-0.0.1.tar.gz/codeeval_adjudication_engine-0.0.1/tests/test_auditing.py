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
from datetime import datetime

from codeeval_adjudication_engine.auditing import DatabaseAuditLogger
from codeeval_adjudication_engine.models import (
    OverrideAuditLog,
    TGSFinalizationAuditLog,
    VoteAuditLog,
    VoteDecision,
)
from tests.mocks import MockDataAccessLayer


class TestDatabaseAuditLogger(unittest.TestCase):
    """
    Test suite for the DatabaseAuditLogger.

    These tests verify that the logger correctly implements the AuditLogger
    interface and persists structured log entries via the DataAccessLayer.
    """

    def setUp(self):
        """Set up a fresh mock DAL and logger for each test."""
        self.mock_dal = MockDataAccessLayer()
        self.logger = DatabaseAuditLogger(dal=self.mock_dal)

    def test_log_vote_action_creates_and_persists_log_entry(self):
        """
        Verify that log_vote_action creates a correctly structured VoteAuditLog
        and passes it to the DAL for persistence.
        Covers FRD NFR-AL5.
        """
        # Arrange
        user_id = "adjudicator-1"
        concept_id = 101
        clinical_idea_id = 1
        decision = VoteDecision.INCLUDE

        # Act
        self.logger.log_vote_action(
            user_id=user_id,
            concept_id=concept_id,
            clinical_idea_id=clinical_idea_id,
            decision=decision,
        )

        # Assert
        self.assertEqual(len(self.mock_dal.vote_audit_log_entries), 1)
        log_entry = self.mock_dal.vote_audit_log_entries[0]

        self.assertIsInstance(log_entry, VoteAuditLog)
        self.assertEqual(log_entry.user_id, user_id)
        self.assertEqual(log_entry.concept_id, concept_id)
        self.assertEqual(log_entry.clinical_idea_id, clinical_idea_id)
        self.assertEqual(log_entry.decision, decision)
        self.assertIsInstance(log_entry.timestamp, datetime)
        # Check that the timestamp is recent (e.g., within the last minute)
        self.assertAlmostEqual(
            log_entry.timestamp.timestamp(), datetime.now().timestamp(), delta=60
        )

    def test_log_override_action_creates_and_persists_log_entry(self):
        """
        Verify that log_override_action creates a correctly structured OverrideAuditLog
        and passes it to the DAL for persistence.
        Covers FRD AL7.6.
        """
        # Arrange
        session_lead_id = "lead-1"
        affected_adjudicator_id = "adjudicator-2"
        action = "DEACTIVATE"
        clinical_idea_id = 2

        # Act
        self.logger.log_override_action(
            session_lead_id=session_lead_id,
            affected_adjudicator_id=affected_adjudicator_id,
            action=action,
            clinical_idea_id=clinical_idea_id,
        )

        # Assert
        self.assertEqual(len(self.mock_dal.override_audit_log_entries), 1)
        log_entry = self.mock_dal.override_audit_log_entries[0]

        self.assertIsInstance(log_entry, OverrideAuditLog)
        self.assertEqual(log_entry.session_lead_id, session_lead_id)
        self.assertEqual(log_entry.affected_adjudicator_id, affected_adjudicator_id)
        self.assertEqual(log_entry.action, action)
        self.assertEqual(log_entry.clinical_idea_id, clinical_idea_id)
        self.assertIsInstance(log_entry.timestamp, datetime)
        # Check that the timestamp is recent
        self.assertAlmostEqual(
            log_entry.timestamp.timestamp(), datetime.now().timestamp(), delta=60
        )

    def test_log_tgs_finalization_creates_and_persists_log_entry(self):
        """
        Verify that log_tgs_finalization creates a correctly structured
        TGSFinalizationAuditLog and passes it to the DAL.
        """
        # Arrange
        clinical_idea_id = 3
        final_tgs_ids = [101, 102, 105]

        # Act
        self.logger.log_tgs_finalization(
            clinical_idea_id=clinical_idea_id,
            final_tgs_concept_ids=final_tgs_ids,
        )

        # Assert
        self.assertEqual(len(self.mock_dal.tgs_finalization_audit_log_entries), 1)
        log_entry = self.mock_dal.tgs_finalization_audit_log_entries[0]

        self.assertIsInstance(log_entry, TGSFinalizationAuditLog)
        self.assertEqual(log_entry.clinical_idea_id, clinical_idea_id)
        self.assertEqual(log_entry.final_tgs_concept_ids, final_tgs_ids)
        self.assertIsInstance(log_entry.timestamp, datetime)
        self.assertAlmostEqual(
            log_entry.timestamp.timestamp(), datetime.now().timestamp(), delta=60
        )


if __name__ == "__main__":
    unittest.main()
