# Copyright (c) 2025-2026 Gowtham A Rao MD PhD. All Rights Reserved.
#
# This software is proprietary and dual-licensed.
# Licensed under the Prosperity Public License 3.0.0 (the "License").
# A copy of the license is available at https://prosperitylicense.com/versions/3.0.0
# For details, see the LICENSE file.
#
# Commercial use beyond a 30-day trial requires a separate license.
# Contact: rao@ohdsi.org

from unittest.mock import patch

from src.codeeval_adjudication_engine.notifiers import LoggingTGSFinalizationNotifier


def test_logging_notifier_sends_correct_log_message():
    """
    Verifies FRD AL5.4 - The notifier must send a clear signal.

    This test ensures that the `LoggingTGSFinalizationNotifier` correctly
    formats and sends a log message when its `notify_tgs_ready` method is called.
    """
    # Arrange: Create an instance of the notifier.
    notifier = LoggingTGSFinalizationNotifier()
    test_clinical_idea_id = 123

    # Act & Assert: Patch the logger to intercept the call.
    # We patch the logger specifically within the 'notifiers' module where it's defined.
    with patch("src.codeeval_adjudication_engine.notifiers.logger") as mock_logger:
        notifier.notify_tgs_ready(test_clinical_idea_id)

        # Assert that the logger's 'info' method was called exactly once.
        mock_logger.info.assert_called_once()

        # Get the arguments passed to the 'info' method.
        # call_args is a tuple where the first element is a tuple of positional args
        # and the second element is a dict of keyword args.
        args, _ = mock_logger.info.call_args

        # Assert the message format and the parameter are correct.
        assert len(args) == 2
        assert (
            args[0]
            == "TGS_FINALIZED: True Gold Standard for clinical_idea_id=%d is ready."
        )
        assert args[1] == test_clinical_idea_id
