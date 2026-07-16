"""
MongoDB Configuration

Centralized MongoDB configuration used across the project.
"""
import os

# ==========================================================
# Connection
# ==========================================================

MONGODB_URI = os.getenv("MONGO_URI")


# ==========================================================
# Database
# ==========================================================

DATABASE_NAME = "architecture_review"


# ==========================================================
# Collections
# ==========================================================

REVIEW_COLLECTION = "reviews"


# ==========================================================
# Connection Settings
# ==========================================================

SERVER_SELECTION_TIMEOUT_MS = 5000

CONNECT_TIMEOUT_MS = 5000

SOCKET_TIMEOUT_MS = 5000


# ==========================================================
# Review Metadata
# ==========================================================

REVIEW_VERSION = "1.0"