# scripts/logging.py
"""Logging utils."""

import logging
from typing import Final

from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

COLORS: Final[dict[str, str]] = {
    "DEBUG": Fore.LIGHTBLACK_EX,
    "INFO": "",
    "WARNING": Fore.YELLOW,
    "ERROR": Fore.RED,
    "CRITICAL": Fore.RED + Style.BRIGHT,
}


class ColoredFormatter(logging.Formatter):
    """Custom formatter to add colors to log messages."""

    def format(self: "ColoredFormatter", record: logging.LogRecord) -> str:
        """Format the log message with color."""
        if record.levelno == logging.ERROR:
            record.msg = f"ERROR: {record.msg}"

        log_message = super().format(record)
        return f"{COLORS.get(record.levelname, '')}{log_message}{Style.RESET_ALL}"


# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create console handler
handler = logging.StreamHandler()

# Create formatter
formatter = ColoredFormatter("%(message)s")

# Add formatter to the handler
handler.setFormatter(formatter)

# Add handler to logger
logger.addHandler(handler)
