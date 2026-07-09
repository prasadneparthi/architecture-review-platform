"""
Logging Configuration

Centralized logging constants.
"""

# ==========================================================
# Logger
# ==========================================================

LOGGER_NAME = "architecture_review"

LOG_LEVEL = "INFO"

# ==========================================================
# Log Files
# ==========================================================

LOG_DIRECTORY = "logs"

APPLICATION_LOG = "application.log"

ERROR_LOG = "error.log"

# ==========================================================
# Rotation
# ==========================================================

MAX_LOG_SIZE = 5 * 1024 * 1024      # 5 MB

BACKUP_COUNT = 5

# ==========================================================
# Log Format
# ==========================================================

LOG_FORMAT = (
    "%(asctime)s | "
    "%(levelname)s | "
    "%(name)s | "
    "%(message)s"
)

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"