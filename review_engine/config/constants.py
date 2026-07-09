ARCHITECTURE_TYPES = [
    "Monolith",
    "Microservices",
    "Event Driven",
    "Serverless",
]

DEPLOYMENT_TYPES = [
    "Cloud",
    "On-Premise",
    "Hybrid",
]

DATABASE_TYPES = [
    "MongoDB",
    "PostgreSQL",
    "MySQL",
    "Oracle",
    "SQL Server",
    "Redis",
]

CACHE_TYPES = [
    "Redis",
    "Memcached",
]

MESSAGE_QUEUE_TYPES = [
    "RabbitMQ",
    "Kafka",
    "AWS SQS",
    "Azure Service Bus",
    "Google Pub/Sub",
    "Redis Streams",
    "Other",
]

AUTHENTICATION_TYPES = [
    "JWT",
    "OAuth2",
    "API Key",
    "Session",
    "Basic Auth",
    "Other",
]

AUTHORIZATION_MODELS = [
    "RBAC",
    "ABAC",
    "PBAC",
    "ACL",
    "Other",
]

CLOUD_PROVIDERS = [
    "AWS",
    "Azure",
    "GCP",
    "Others",
]

REVIEW_CATEGORIES = [
    "Scalability",
    "Security",
    "Reliability",
    "Performance",
    "Maintainability",
    "Cost Efficiency",
]

RULE_SEVERITIES = [
    "Critical",
    "High",
    "Medium",
    "Low",
]

RULE_STATUS = [
    "PASS",
    "FAIL",
    "NOT_EVALUATED",
]

YES_NO_VALUES = [
    "Yes",
    "No",
]

MAX_SCORE = 100
MIN_SCORE = 0

DEFAULT_LLM = "Gemini"

DEFAULT_REVIEW_VERSION = "1.0"
DEFAULT_RULEBOOK_VERSION = "1.0"
DEFAULT_SCHEMA_VERSION = "1.1"