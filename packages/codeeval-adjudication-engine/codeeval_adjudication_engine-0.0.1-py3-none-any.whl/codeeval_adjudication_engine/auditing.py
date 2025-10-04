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

from .interfaces import AuditLogger, DataAccessLayer
from .models import (
    OverrideAuditLog,
    TGSFinalizationAuditLog,
    VoteAuditLog,
    VoteDecision,
)


class DatabaseAuditLogger(AuditLogger):
    """
    A concrete implementation of the AuditLogger that persists audit trails
    to the database via the DataAccessLayer.

    This implementation ensures that audit records are created within the same
    transactional context as the actions they are recording, providing a high
    degree of data integrity as required by the FRD.
    """

    def __init__(self, dal: DataAccessLayer):
        """
        Initializes the DatabaseAuditLogger.

        Args:
            dal: An object conforming to the DataAccessLayer interface, used for
                 persisting the audit log entries.
        """
        self._dal = dal
        self._log_id_counter = 0  # Simple counter for mock log IDs

    def _get_next_log_id(self) -> int:
        """Generates a placeholder log ID."""
        self._log_id_counter += 1
        return self._log_id_counter

    def log_vote_action(
        self,
        user_id: str,
        concept_id: int,
        clinical_idea_id: int,
        decision: VoteDecision,
    ) -> None:
        """
        Logs a vote action by creating a VoteAuditLog entry and persisting it
        through the Data Access Layer.

        Fulfills FRD NFR-AL5.
        """
        log_entry = VoteAuditLog(
            log_id=self._get_next_log_id(),
            user_id=user_id,
            concept_id=concept_id,
            clinical_idea_id=clinical_idea_id,
            decision=decision,
            timestamp=datetime.now(timezone.utc),
        )
        self._dal.create_vote_audit_log(log_entry)

    def log_override_action(
        self,
        session_lead_id: str,
        affected_adjudicator_id: str,
        action: str,
        clinical_idea_id: int,
    ) -> None:
        """
        Logs an operational override action by creating an OverrideAuditLog entry
        and persisting it through the Data Access Layer.

        Fulfills FRD AL7.6.
        """
        log_entry = OverrideAuditLog(
            log_id=self._get_next_log_id(),
            session_lead_id=session_lead_id,
            affected_adjudicator_id=affected_adjudicator_id,
            action=action,
            clinical_idea_id=clinical_idea_id,
            timestamp=datetime.now(timezone.utc),
        )
        self._dal.create_override_audit_log(log_entry)

    def log_tgs_finalization(
        self,
        clinical_idea_id: int,
        final_tgs_concept_ids: List[int],
    ) -> None:
        """
        Logs a TGS finalization event by creating a TGSFinalizationAuditLog
        entry and persisting it through the Data Access Layer.
        """
        log_entry = TGSFinalizationAuditLog(
            log_id=self._get_next_log_id(),
            clinical_idea_id=clinical_idea_id,
            timestamp=datetime.now(timezone.utc),
            final_tgs_concept_ids=final_tgs_concept_ids,
        )
        self._dal.create_tgs_finalization_audit_log(log_entry)
