"""
Cost Analysis Constants

Defines the internal weighted cost model.

These are relative cost weights,
NOT real cloud pricing.
"""

# ==========================================================
# Base Score
# ==========================================================

MAX_COST_SCORE = 100
MIN_COST_SCORE = 0


# ==========================================================
# Infrastructure Cost Weights
# ==========================================================

SERVICE_WEIGHT = 2
INSTANCE_WEIGHT = 2

LOAD_BALANCER_WEIGHT = 3

CACHE_WEIGHT = 5

MESSAGE_QUEUE_WEIGHT = 5

DATABASE_WEIGHT = 5

REPLICATION_WEIGHT = 8

READ_REPLICA_WEIGHT = 5

SHARDING_WEIGHT = 10

MONITORING_WEIGHT = 2

BACKUP_WEIGHT = 3

DR_WEIGHT = 5


# ==========================================================
# Cost Rating Thresholds
# ==========================================================

VERY_LOW_COST = 90
LOW_COST = 75
MEDIUM_COST = 60
HIGH_COST = 40


# ==========================================================
# Cost Ratings
# ==========================================================

VERY_LOW = "Very Low"

LOW = "Low"

MEDIUM = "Medium"

HIGH = "High"

VERY_HIGH = "Very High"