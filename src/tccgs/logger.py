"""Configure the root logger."""

from __future__ import annotations

import atexit
import logging
import logging.config
import logging.handlers
import time
import tomllib
from typing import Any, override

from tccgs.config import LOGGER_CONFIG_FILE, PACKAGE_NAME

ROOT_LOGGER_NAME = PACKAGE_NAME

__all__ = ("ROOT_LOGGER_NAME", "setup_logging")


# Remove if/when the TOML file works for Nuitka too.
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "[%(levelname)s|%(module)s|L%(lineno)d] %(asctime)s: %(message)s",
            "datefmt": "%Y-%m-%dT%H:%M:%S%z",
        },
        "colour": {
            "format": "%(asctime)s.%(msecs)03.0fZ [%(levelname)s] %(module)s:L%(lineno)04d | %(funcName)s: %(message)s",
            "class": "tccgs.logger.ColouredFormatter",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "stdout": {
            "level": "INFO",
            "formatter": "colour",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
        "stderr": {
            "level": "WARNING",
            "formatter": "simple",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
        "queue_handler": {
            "level": "INFO",
            "class": "tccgs.logger.CustomQueueHandler",
            "handlers": ["stdout"],
            "respect_handler_level": True,
        },
    },
    "loggers": {
        "": {  # root logger
            "handlers": ["queue_handler"],
            "level": "DEBUG",
        },
    },
}


class ColouredFormatter(logging.Formatter):
    """Coloured log formatter."""

    # This enforces UTC timestamps regardless of local timezone
    # and is necessary for easier log comparisons
    converter = time.gmtime

    @override
    def format(self, record: logging.LogRecord) -> str:
        """Format the log record."""
        log_level_colours = {
            logging.CRITICAL: "\033[31;1m",  # Red, bold
            logging.ERROR: "\033[31m",  # Red
            logging.WARNING: "\033[33m",  # Yellow
            logging.INFO: "\033[32m",  # Green
            logging.DEBUG: "\033[34m",  # Cyan
        }
        reset = "\033[0m"

        record.module = ROOT_LOGGER_NAME
        record.msg = f"{log_level_colours.get(record.levelno, reset)}{record.msg}{reset}"
        record.levelname = f"{log_level_colours.get(record.levelno, reset)}{record.levelname:^8}{reset}"

        return super().format(record)


class CustomQueueHandler(logging.handlers.QueueHandler):
    """Custom queue handler."""

    @override
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        queue_handler = logging.getHandlerByName("queue_handler")
        if queue_handler is None:
            super().__init__(*args, **kwargs)  # type: ignore[arg-type]


def setup_logging() -> None:
    """Set up logging."""
    try:
        logger_data = LOGGER_CONFIG_FILE.read_text(encoding="utf-8")
    except FileNotFoundError:
        # This currently happens in Nuitka builds as the file can't be read
        logging.config.dictConfig(LOGGING_CONFIG)
    else:
        logging_config = tomllib.loads(logger_data)
        logging.config.dictConfig(logging_config)

    queue_handler = logging.getHandlerByName("queue_handler")
    if queue_handler is not None:
        queue_handler.listener.start()  # type: ignore[attr-defined]
        atexit.register(queue_handler.listener.stop)  # type: ignore[attr-defined]
