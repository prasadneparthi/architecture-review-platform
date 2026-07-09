from rest_framework import serializers

from review_engine.config.constants import (
    ARCHITECTURE_TYPES,
    DATABASE_TYPES,
    CACHE_TYPES,
    MESSAGE_QUEUE_TYPES,
    AUTHENTICATION_TYPES,
    AUTHORIZATION_MODELS,
)


# ==========================================================
# Services
# ==========================================================

class ServiceSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    technology = serializers.CharField(max_length=100)
    instances = serializers.IntegerField(min_value=1)
    stateless = serializers.BooleanField()
    async_processing = serializers.BooleanField()


# ==========================================================
# Databases
# ==========================================================

class DatabaseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    type = serializers.ChoiceField(choices=DATABASE_TYPES)
    replication = serializers.BooleanField()
    read_replicas = serializers.BooleanField(required=False)
    sharding = serializers.BooleanField(required=False)
    indexes = serializers.BooleanField()
    connection_pooling = serializers.BooleanField()


# ==========================================================
# Load Balancer
# ==========================================================

class LoadBalancerSerializer(serializers.Serializer):
    enabled = serializers.BooleanField()
    health_checks = serializers.BooleanField(required=False)


# ==========================================================
# Cache
# ==========================================================

class CacheSerializer(serializers.Serializer):
    enabled = serializers.BooleanField()
    type = serializers.ChoiceField(
        choices=CACHE_TYPES,
        required=False,
        allow_null=True,
    )
    invalidation_strategy = serializers.BooleanField(required=False)


# ==========================================================
# Message Queue
# ==========================================================

class MessageQueueSerializer(serializers.Serializer):
    enabled = serializers.BooleanField()
    type = serializers.ChoiceField(
        choices=MESSAGE_QUEUE_TYPES,
        required=False,
        allow_null=True,
    )
    retry_enabled = serializers.BooleanField()


# ==========================================================
# Security
# ==========================================================

class SecuritySerializer(serializers.Serializer):
    authentication = serializers.BooleanField()
    authentication_type = serializers.ChoiceField(
        choices=AUTHENTICATION_TYPES
    )

    authorization = serializers.BooleanField()
    authorization_model = serializers.ChoiceField(
        choices=AUTHORIZATION_MODELS
    )

    https = serializers.BooleanField()
    encrypt_at_rest = serializers.BooleanField()

    rate_limiting = serializers.BooleanField()
    input_validation = serializers.BooleanField()

    secret_management = serializers.BooleanField()
    default_credentials = serializers.BooleanField()

    cors = serializers.BooleanField(required=False)
    security_headers = serializers.BooleanField(required=False)


# ==========================================================
# Monitoring
# ==========================================================

class MonitoringSerializer(serializers.Serializer):
    enabled = serializers.BooleanField()
    centralized_logging = serializers.BooleanField()
    alerting = serializers.BooleanField(required=False)
    status_endpoint = serializers.BooleanField(required=False)


# ==========================================================
# Resilience
# ==========================================================

class ResilienceSerializer(serializers.Serializer):
    retry_enabled = serializers.BooleanField()
    timeouts = serializers.BooleanField()
    circuit_breaker = serializers.BooleanField(required=False)
    graceful_degradation = serializers.BooleanField(required=False)


# ==========================================================
# Backup
# ==========================================================

class BackupSerializer(serializers.Serializer):
    enabled = serializers.BooleanField()
    restore_tested = serializers.BooleanField()
    rto_rpo_defined = serializers.BooleanField(required=False)
    dr_documented = serializers.BooleanField(required=False)


# ==========================================================
# API
# ==========================================================

class APISerializer(serializers.Serializer):
    pagination = serializers.BooleanField()
    compression = serializers.BooleanField(required=False)
    versioning = serializers.BooleanField(required=False)


# ==========================================================
# Deployment
# ==========================================================

class DeploymentSerializer(serializers.Serializer):
    rollback = serializers.BooleanField()
    cicd = serializers.BooleanField()
    repeatable_releases = serializers.BooleanField()
    zero_downtime = serializers.BooleanField(required=False)
    safe_db_migration = serializers.BooleanField(required=False)


# ==========================================================
# Architecture
# ==========================================================

class ArchitectureDetailsSerializer(serializers.Serializer):
    layered_design = serializers.BooleanField()
    separation_of_concerns = serializers.BooleanField()
    interface_definition = serializers.BooleanField(required=False)
    loose_coupling = serializers.BooleanField()


# ==========================================================
# Testing
# ==========================================================

class TestingSerializer(serializers.Serializer):
    unit_tests = serializers.BooleanField()
    integration_tests = serializers.BooleanField()
    api_tests = serializers.BooleanField(required=False)
    component_testability = serializers.BooleanField()


# ==========================================================
# Documentation
# ==========================================================

class DocumentationSerializer(serializers.Serializer):
    api_docs = serializers.BooleanField()
    architecture_docs = serializers.BooleanField()
    deployment_docs = serializers.BooleanField(required=False)
    operations_docs = serializers.BooleanField(required=False)


# ==========================================================
# Configuration
# ==========================================================

class ConfigurationSerializer(serializers.Serializer):
    externalized = serializers.BooleanField()
    environment_support = serializers.BooleanField()
    centralized = serializers.BooleanField(required=False)
    no_hardcoded_values = serializers.BooleanField()


# ==========================================================
# Master Architecture Serializer
# ==========================================================

class ArchitectureSerializer(serializers.Serializer):
    system_name = serializers.CharField(max_length=200)
    architecture_type = serializers.ChoiceField(
        choices=ARCHITECTURE_TYPES
    )

    services = ServiceSerializer(many=True)
    databases = DatabaseSerializer(many=True)

    load_balancer = LoadBalancerSerializer()

    cache = CacheSerializer()

    message_queue = MessageQueueSerializer()

    security = SecuritySerializer()

    monitoring = MonitoringSerializer()

    resilience = ResilienceSerializer()

    backup = BackupSerializer()

    api = APISerializer()

    deployment = DeploymentSerializer()

    architecture = ArchitectureDetailsSerializer()

    testing = TestingSerializer()

    documentation = DocumentationSerializer()

    configuration = ConfigurationSerializer()