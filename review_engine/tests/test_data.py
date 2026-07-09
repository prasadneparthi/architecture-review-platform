"""
Reusable test data for the Architecture Review project.

Provides valid architecture input that can be modified
inside individual test cases.
"""

import copy


_VALID_ARCHITECTURE = {
    "system_name": "E-Commerce Platform",
    "architecture_type": "Microservices",

    "services": [
        {
            "name": "User Service",
            "technology": "Django",
            "instances": 2,
            "stateless": True,
            "async_processing": True,
        }
    ],

    "databases": [
        {
            "name": "MongoDB",
            "type": "MongoDB",
            "replication": True,
            "read_replicas": True,
            "sharding": True,
            "indexes": True,
            "connection_pooling": True,
        }
    ],

    "load_balancer": {
        "enabled": True,
        "health_checks": True,
    },

    "cache": {
        "enabled": True,
        "type": "Redis",
        "invalidation_strategy": True,
    },

    "message_queue": {
        "enabled": True,
        "type": "RabbitMQ",
        "retry_enabled": True,
    },

    "security": {
        "authentication": True,
        "authentication_type": "JWT",

        "authorization": True,
        "authorization_model": "RBAC",

        "https": True,
        "encrypt_at_rest": True,

        "rate_limiting": True,
        "input_validation": True,

        "secret_management": True,
        "default_credentials": False,

        "cors": True,
        "security_headers": True,
    },

    "monitoring": {
        "enabled": True,
        "centralized_logging": True,
        "alerting": True,
        "status_endpoint": True,
    },

    "resilience": {
        "retry_enabled": True,
        "timeouts": True,
        "circuit_breaker": True,
        "graceful_degradation": True,
    },

    "backup": {
        "enabled": True,
        "restore_tested": True,
        "rto_rpo_defined": True,
        "dr_documented": True,
    },

    "api": {
        "pagination": True,
        "compression": True,
        "versioning": True,
    },

    "deployment": {
        "rollback": True,
        "cicd": True,
        "repeatable_releases": True,
        "zero_downtime": True,
        "safe_db_migration": True,
    },

    "architecture": {
        "layered_design": True,
        "separation_of_concerns": True,
        "interface_definition": True,
        "loose_coupling": True,
    },

    "testing": {
        "unit_tests": True,
        "integration_tests": True,
        "api_tests": True,
        "component_testability": True,
    },

    "documentation": {
        "api_docs": True,
        "architecture_docs": True,
        "deployment_docs": True,
        "operations_docs": True,
    },

    "configuration": {
        "externalized": True,
        "environment_support": True,
        "centralized": True,
        "no_hardcoded_values": True,
    },
}


def get_valid_architecture():
    """
    Returns a fresh copy of the valid architecture.

    A deep copy is returned so that each test can freely
    modify the data without affecting other tests.
    """

    return copy.deepcopy(_VALID_ARCHITECTURE)