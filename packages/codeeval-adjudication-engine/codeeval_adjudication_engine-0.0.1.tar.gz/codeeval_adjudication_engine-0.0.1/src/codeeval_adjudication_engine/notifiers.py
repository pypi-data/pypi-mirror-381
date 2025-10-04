# Copyright (c) 2025-2026 Gowtham A Rao MD PhD. All Rights Reserved.
#
# This software is proprietary and dual-licensed.
# Licensed under the Prosperity Public License 3.0.0 (the "License").
# A copy of the license is available at https://prosperitylicense.com/versions/3.0.0
# For details, see the LICENSE file.
#
# Commercial use beyond a 30-day trial requires a separate license.
# Contact: rao@ohdsi.org

import logging

from .interfaces import TGSFinalizationNotifier

# It is best practice to get the logger for the specific module.
logger = logging.getLogger(__name__)


class LoggingTGSFinalizationNotifier(TGSFinalizationNotifier):
    """
    A concrete implementation of the TGSFinalizationNotifier that logs the
    notification to a standard Python logger.

    This fulfills FRD AL5.4 by providing a decoupled notification mechanism.
    """

    def notify_tgs_ready(self, clinical_idea_id: int) -> None:
        """
        Logs a structured message indicating that the TGS is ready.

        Args:
            clinical_idea_id: The ID of the finalized clinical idea.
        """
        logger.info(
            "TGS_FINALIZED: True Gold Standard for clinical_idea_id=%d is ready.",
            clinical_idea_id,
        )
