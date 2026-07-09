"""
Architecture Input Schema

Schema definitions only.
No validation or business logic.
"""

from review_engine.config.constants import (
    ARCHITECTURE_TYPES,
    DATABASE_TYPES,
    CACHE_TYPES,
    MESSAGE_QUEUE_TYPES,
    AUTHENTICATION_TYPES,
    AUTHORIZATION_MODELS,
)

# ==========================================================
# Required / Optional Top-Level Fields
# ==========================================================

REQUIRED_FIELDS = (
    "system_name",
    "architecture_type",
    "services",
    "databases",
    "load_balancer",
    "cache",
    "message_queue",
    "security",
    "monitoring",
    "resilience",
    "backup",
    "api",
    "deployment",
    "architecture",
    "testing",
    "documentation",
    "configuration",
)

OPTIONAL_FIELDS = ()

# ==========================================================
# Services
# ==========================================================

SERVICE_SCHEMA = {
    "name": str,
    "technology": str,
    "instances": int,
    "stateless": bool,
    "async_processing": bool,
}

# ==========================================================
# Databases
# ==========================================================

DATABASE_SCHEMA = {
    "name": str,
    "type": DATABASE_TYPES,
    "replication": bool,
    "read_replicas": bool,
    "sharding": bool,
    "indexes": bool,
    "connection_pooling": bool,
}

# ==========================================================
# Load Balancer
# ==========================================================

LOAD_BALANCER_SCHEMA = {
    "enabled": bool,
    "health_checks": bool,
}

# ==========================================================
# Cache
# ==========================================================

CACHE_SCHEMA = {
    "enabled": bool,
    "type": CACHE_TYPES,
    "invalidation_strategy": bool,
}

# ==========================================================
# Message Queue
# ==========================================================

MESSAGE_QUEUE_SCHEMA = {
    "enabled": bool,
    "type": MESSAGE_QUEUE_TYPES,
    "retry_enabled": bool,
}

# ==========================================================
# Security
# ==========================================================

SECURITY_SCHEMA = {
    "authentication": bool,
    "authentication_type": AUTHENTICATION_TYPES,
    "authorization": bool,
    "authorization_model": AUTHORIZATION_MODELS,
    "https": bool,
    "encrypt_at_rest": bool,
    "rate_limiting": bool,
    "input_validation": bool,
    "secret_management": bool,
    "default_credentials": bool,
    "cors": bool,
    "security_headers": bool,
}

# ==========================================================
# Monitoring
# ==========================================================

MONITORING_SCHEMA = {
    "enabled": bool,
    "centralized_logging": bool,
    "alerting": bool,
    "status_endpoint": bool,
}

# ==========================================================
# Resilience
# ==========================================================

RESILIENCE_SCHEMA = {
    "retry_enabled": bool,
    "timeouts": bool,
    "circuit_breaker": bool,
    "graceful_degradation": bool,
}

# ==========================================================
# Backup
# ==========================================================

BACKUP_SCHEMA = {
    "enabled": bool,
    "restore_tested": bool,
    "rto_rpo_defined": bool,
    "dr_documented": bool,
}

# ==========================================================
# API
# ==========================================================

API_SCHEMA = {
    "pagination": bool,
    "compression": bool,
    "versioning": bool,
}

# ==========================================================
# Deployment
# ==========================================================

DEPLOYMENT_SCHEMA = {
    "rollback": bool,
    "cicd": bool,
    "repeatable_releases": bool,
    "zero_downtime": bool,
    "safe_db_migration": bool,
}

# ==========================================================
# Architecture
# ==========================================================

ARCHITECTURE_DETAILS_SCHEMA = {
    "layered_design": bool,
    "separation_of_concerns": bool,
    "interface_definition": bool,
    "loose_coupling": bool,
}

# ==========================================================
# Testing
# ==========================================================

TESTING_SCHEMA = {
    "unit_tests": bool,
    "integration_tests": bool,
    "api_tests": bool,
    "component_testability": bool,
}

# ==========================================================
# Documentation
# ==========================================================

DOCUMENTATION_SCHEMA = {
    "api_docs": bool,
    "architecture_docs": bool,
    "deployment_docs": bool,
    "operations_docs": bool,
}

# ==========================================================
# Configuration
# ==========================================================

CONFIGURATION_SCHEMA = {
    "externalized": bool,
    "environment_support": bool,
    "centralized": bool,
    "no_hardcoded_values": bool,
}

# ==========================================================
# Master Schema
# ==========================================================

ARCHITECTURE_SCHEMA = {
    "system_name": str,
    "architecture_type": ARCHITECTURE_TYPES,
    "services": [SERVICE_SCHEMA],
    "databases": [DATABASE_SCHEMA],
    "load_balancer": LOAD_BALANCER_SCHEMA,
    "cache": CACHE_SCHEMA,
    "message_queue": MESSAGE_QUEUE_SCHEMA,
    "security": SECURITY_SCHEMA,
    "monitoring": MONITORING_SCHEMA,
    "resilience": RESILIENCE_SCHEMA,
    "backup": BACKUP_SCHEMA,
    "api": API_SCHEMA,
    "deployment": DEPLOYMENT_SCHEMA,
    "architecture": ARCHITECTURE_DETAILS_SCHEMA,
    "testing": TESTING_SCHEMA,
    "documentation": DOCUMENTATION_SCHEMA,
    "configuration": CONFIGURATION_SCHEMA,
}