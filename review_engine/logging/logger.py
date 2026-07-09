"""
Application Logger

Provides a singleton logger for the Architecture Review project.

Responsibilities
----------------
- Console logging
- File logging
- Error logging
- Log rotation

Does NOT
--------
- Perform business logic
"""

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from review_engine.config.logging_constants import (
    LOGGER_NAME,
    LOG_LEVEL,
    LOG_DIRECTORY,
    APPLICATION_LOG,
    ERROR_LOG,
    MAX_LOG_SIZE,
    BACKUP_COUNT,
    LOG_FORMAT,
    DATE_FORMAT,
)


class logger:

    _logger = None

    @classmethod
    def get_logger(cls):

        if cls._logger is not None:
            return cls._logger

        # -------------------------------------------------
        # Create logs directory
        # -------------------------------------------------

        log_directory = Path(LOG_DIRECTORY)

        log_directory.mkdir(
            exist_ok=True
        )

        # -------------------------------------------------
        # Logger
        # -------------------------------------------------

        logger = logging.getLogger(
            LOGGER_NAME
        )

        logger.setLevel(
            getattr(logging, LOG_LEVEL)
        )

        logger.propagate = False

        if logger.handlers:
            cls._logger = logger
            return logger

        # -------------------------------------------------
        # Formatter
        # -------------------------------------------------

        formatter = logging.Formatter(
            LOG_FORMAT,
            DATE_FORMAT,
        )

        # -------------------------------------------------
        # Console Handler
        # -------------------------------------------------

        console_handler = logging.StreamHandler()

        console_handler.setFormatter(
            formatter
        )

        # -------------------------------------------------
        # Application Log
        # -------------------------------------------------

        application_handler = RotatingFileHandler(
            log_directory / APPLICATION_LOG,
            maxBytes=MAX_LOG_SIZE,
            backupCount=BACKUP_COUNT,
            encoding="utf-8",
        )

        application_handler.setLevel(
            logging.INFO
        )

        application_handler.setFormatter(
            formatter
        )

        # -------------------------------------------------
        # Error Log
        # -------------------------------------------------

        error_handler = RotatingFileHandler(
            log_directory / ERROR_LOG,
            maxBytes=MAX_LOG_SIZE,
            backupCount=BACKUP_COUNT,
            encoding="utf-8",
        )

        error_handler.setLevel(
            logging.ERROR
        )

        error_handler.setFormatter(
            formatter
        )

        # -------------------------------------------------
        # Register Handlers
        # -------------------------------------------------

        logger.addHandler(
            console_handler
        )

        logger.addHandler(
            application_handler
        )

        logger.addHandler(
            error_handler
        )

        cls._logger = logger

        return logger