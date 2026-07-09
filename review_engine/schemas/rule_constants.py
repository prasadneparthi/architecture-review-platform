"""
Architecture Review Rule Book v1.0

Frozen Rule Definitions

This file contains ONLY rule metadata.

No evaluation logic should be added here.
"""

# ==========================================================
# Rule Severities
# ==========================================================

CRITICAL = "Critical"
HIGH = "High"
MEDIUM = "Medium"
LOW = "Low"

# ==========================================================
# Rule Categories
# ==========================================================

SCALABILITY = "Scalability"
SECURITY = "Security"
RELIABILITY = "Reliability"
PERFORMANCE = "Performance"
MAINTAINABILITY = "Maintainability"

# ==========================================================
# Rule Types
# ==========================================================

BOOLEAN = "BOOLEAN"
INTEGER = "INTEGER"
EXISTS = "EXISTS"

# ==========================================================
# Rule Book
# ==========================================================

RULES = [

    # ======================================================
    # SCALABILITY
    # ======================================================

    {
        "id": "SCA_001",
        "category": SCALABILITY,
        "principle": "Horizontal Scaling",
        "title": "Services should support multiple instances",
        "severity": CRITICAL,
        "type": INTEGER,
        "json_path": "services[].instances",
        "expected": 2,
        "recommendation": "Deploy at least two instances for every critical service.",
    },

    {
        "id": "SCA_002",
        "category": SCALABILITY,
        "principle": "Horizontal Scaling",
        "title": "Services should be stateless",
        "severity": HIGH,
        "type": BOOLEAN,
        "json_path": "services[].stateless",
        "expected": True,
        "recommendation": "Design services to be stateless for easier scaling.",
    },

    {
        "id": "SCA_003",
        "category": SCALABILITY,
        "principle": "Horizontal Scaling",
        "title": "User sessions should not be stored locally",
        "severity": HIGH,
        "type": EXISTS,
        "json_path": "services[].stateless",
        "expected": True,
        "recommendation": "Store session information in shared storage.",
    },

    {
        "id": "SCA_004",
        "category": SCALABILITY,
        "principle": "Horizontal Scaling",
        "title": "Asynchronous processing should be supported",
        "severity": HIGH,
        "type": BOOLEAN,
        "json_path": "services[].async_processing",
        "expected": True,
        "recommendation": "Move long-running tasks to asynchronous workers.",
    },

    {
        "id": "SCA_005",
        "category": SCALABILITY,
        "principle": "Traffic Distribution",
        "title": "Load balancer should exist",
        "severity": CRITICAL,
        "type": BOOLEAN,
        "json_path": "load_balancer.enabled",
        "expected": True,
        "recommendation": "Use a load balancer to distribute incoming traffic.",
    },

    {
        "id": "SCA_006",
        "category": SCALABILITY,
        "principle": "Traffic Distribution",
        "title": "Message queue should be available",
        "severity": HIGH,
        "type": BOOLEAN,
        "json_path": "message_queue.enabled",
        "expected": True,
        "recommendation": "Introduce a message queue for asynchronous communication.",
    },

    {
        "id": "SCA_007",
        "category": SCALABILITY,
        "principle": "Traffic Distribution",
        "title": "Load balancer health checks should exist",
        "severity": MEDIUM,
        "type": BOOLEAN,
        "json_path": "load_balancer.health_checks",
        "expected": True,
        "recommendation": "Enable health checks for backend instances.",
    },

    {
        "id": "SCA_008",
        "category": SCALABILITY,
        "principle": "Traffic Distribution",
        "title": "Traffic should pass through a centralized load balancer",
        "severity": MEDIUM,
        "type": BOOLEAN,
        "json_path": "load_balancer.enabled",
        "expected": True,
        "recommendation": "Route client traffic through the load balancer.",
    },

    {
        "id": "SCA_009",
        "category": SCALABILITY,
        "principle": "Database Scaling",
        "title": "Database replication should exist",
        "severity": CRITICAL,
        "type": BOOLEAN,
        "json_path": "databases[].replication",
        "expected": True,
        "recommendation": "Enable database replication.",
    },

    {
        "id": "SCA_010",
        "category": SCALABILITY,
        "principle": "Database Scaling",
        "title": "Read replicas should exist",
        "severity": MEDIUM,
        "type": BOOLEAN,
        "json_path": "databases[].read_replicas",
        "expected": True,
        "recommendation": "Use read replicas for read-heavy workloads.",
    },

    {
        "id": "SCA_011",
        "category": SCALABILITY,
        "principle": "Database Scaling",
        "title": "Database sharding should be supported",
        "severity": LOW,
        "type": BOOLEAN,
        "json_path": "databases[].sharding",
        "expected": True,
        "recommendation": "Consider sharding for very large datasets.",
    },

    {
        "id": "SCA_012",
        "category": SCALABILITY,
        "principle": "Database Scaling",
        "title": "Database should support high availability",
        "severity": CRITICAL,
        "type": BOOLEAN,
        "json_path": "databases[].replication",
        "expected": True,
        "recommendation": "Deploy databases in a highly available configuration.",
    },

    {
        "id": "SCA_013",
        "category": SCALABILITY,
        "principle": "Workload Distribution",
        "title": "Message queue should decouple workloads",
        "severity": HIGH,
        "type": BOOLEAN,
        "json_path": "message_queue.enabled",
        "expected": True,
        "recommendation": "Use queues to decouple producers and consumers.",
    },

    {
        "id": "SCA_014",
        "category": SCALABILITY,
        "principle": "Workload Distribution",
        "title": "Background processing should exist",
        "severity": HIGH,
        "type": BOOLEAN,
        "json_path": "services[].async_processing",
        "expected": True,
        "recommendation": "Execute heavy operations asynchronously.",
    },

    {
        "id": "SCA_015",
        "category": SCALABILITY,
        "principle": "Workload Distribution",
        "title": "Workers should scale independently",
        "severity": MEDIUM,
        "type": BOOLEAN,
        "json_path": "message_queue.enabled",
        "expected": True,
        "recommendation": "Separate worker scaling from API scaling.",
    },

    {
        "id": "SCA_016",
        "category": SCALABILITY,
        "principle": "Workload Distribution",
        "title": "Queue retry mechanism should exist",
        "severity": HIGH,
        "type": BOOLEAN,
        "json_path": "message_queue.retry_enabled",
        "expected": True,
        "recommendation": "Configure retry policies for queued jobs.",
    },

    {
        "id": "SCA_017",
        "category": SCALABILITY,
        "principle": "Caching",
        "title": "Caching should be enabled",
        "severity": HIGH,
        "type": BOOLEAN,
        "json_path": "cache.enabled",
        "expected": True,
        "recommendation": "Enable caching to reduce backend load.",
    },

    {
        "id": "SCA_018",
        "category": SCALABILITY,
        "principle": "Caching",
        "title": "Shared cache should be used",
        "severity": MEDIUM,
        "type": BOOLEAN,
        "json_path": "cache.enabled",
        "expected": True,
        "recommendation": "Use a centralized distributed cache.",
    },

    {
        "id": "SCA_019",
        "category": SCALABILITY,
        "principle": "Caching",
        "title": "Cache invalidation strategy should exist",
        "severity": MEDIUM,
        "type": BOOLEAN,
        "json_path": "cache.invalidation_strategy",
        "expected": True,
        "recommendation": "Define a cache invalidation strategy.",
    },

    {
        "id": "SCA_020",
        "category": SCALABILITY,
        "principle": "Caching",
        "title": "Frequently accessed data should be cached",
        "severity": HIGH,
        "type": BOOLEAN,
        "json_path": "cache.enabled",
        "expected": True,
        "recommendation": "Cache frequently requested data.",
    },
        # ======================================================
    # SECURITY
    # ======================================================

    {
        "id": "SEC_001",
        "category": SECURITY,
        "principle": "Authentication",
        "title": "Authentication should be enabled",
        "severity": CRITICAL,
        "type": BOOLEAN,
        "json_path": "security.authentication",
        "expected": True,
        "recommendation": "Enable authentication for all protected resources.",
    },

    {
        "id": "SEC_002",
        "category": SECURITY,
        "principle": "Authentication",
        "title": "Secure authentication mechanism should be used",
        "severity": HIGH,
        "type": EXISTS,
        "json_path": "security.authentication_type",
        "expected": True,
        "recommendation": "Use JWT, OAuth2 or another secure authentication mechanism.",
    },

    {
        "id": "SEC_003",
        "category": SECURITY,
        "principle": "Authentication",
        "title": "Anonymous access should not be allowed",
        "severity": HIGH,
        "type": BOOLEAN,
        "json_path": "security.authentication",
        "expected": True,
        "recommendation": "Protect endpoints from anonymous access.",
    },

    {
        "id": "SEC_004",
        "category": SECURITY,
        "principle": "Authentication",
        "title": "Authentication should be consistently enforced",
        "severity": MEDIUM,
        "type": BOOLEAN,
        "json_path": "security.authentication",
        "expected": True,
        "recommendation": "Ensure authentication is enforced consistently.",
    },

    {
        "id": "SEC_005",
        "category": SECURITY,
        "principle": "Authorization",
        "title": "Authorization should be implemented",
        "severity": CRITICAL,
        "type": BOOLEAN,
        "json_path": "security.authorization",
        "expected": True,
        "recommendation": "Implement authorization checks for protected resources.",
    },

    {
        "id": "SEC_006",
        "category": SECURITY,
        "principle": "Authorization",
        "title": "Role or policy based authorization should exist",
        "severity": HIGH,
        "type": EXISTS,
        "json_path": "security.authorization_model",
        "expected": True,
        "recommendation": "Use RBAC, ABAC or another authorization model.",
    },

    {
        "id": "SEC_007",
        "category": SECURITY,
        "principle": "Authorization",
        "title": "Administrative resources should be protected",
        "severity": HIGH,
        "type": BOOLEAN,
        "json_path": "security.authorization",
        "expected": True,
        "recommendation": "Restrict administrative functionality.",
    },

    {
        "id": "SEC_008",
        "category": SECURITY,
        "principle": "Authorization",
        "title": "Least privilege principle should be followed",
        "severity": MEDIUM,
        "type": BOOLEAN,
        "json_path": "security.authorization",
        "expected": True,
        "recommendation": "Grant only the minimum required permissions.",
    },

    {
        "id": "SEC_009",
        "category": SECURITY,
        "principle": "Data Protection",
        "title": "HTTPS should be enabled",
        "severity": CRITICAL,
        "type": BOOLEAN,
        "json_path": "security.https",
        "expected": True,
        "recommendation": "Enable HTTPS for all endpoints.",
    },

    {
        "id": "SEC_010",
        "category": SECURITY,
        "principle": "Data Protection",
        "title": "Sensitive data should be encrypted at rest",
        "severity": HIGH,
        "type": BOOLEAN,
        "json_path": "security.encrypt_at_rest",
        "expected": True,
        "recommendation": "Encrypt sensitive data stored in databases.",
    },

    {
        "id": "SEC_011",
        "category": SECURITY,
        "principle": "Data Protection",
        "title": "Sensitive data should be encrypted in transit",
        "severity": HIGH,
        "type": BOOLEAN,
        "json_path": "security.https",
        "expected": True,
        "recommendation": "Encrypt all network communication.",
    },

    {
        "id": "SEC_012",
        "category": SECURITY,
        "principle": "Data Protection",
        "title": "Sensitive data exposure should be minimized",
        "severity": MEDIUM,
        "type": BOOLEAN,
        "json_path": "security.encrypt_at_rest",
        "expected": True,
        "recommendation": "Protect sensitive information from unnecessary exposure.",
    },

    {
        "id": "SEC_013",
        "category": SECURITY,
        "principle": "Application Security",
        "title": "Rate limiting should be enabled",
        "severity": HIGH,
        "type": BOOLEAN,
        "json_path": "security.rate_limiting",
        "expected": True,
        "recommendation": "Protect APIs using rate limiting.",
    },

    {
        "id": "SEC_014",
        "category": SECURITY,
        "principle": "Application Security",
        "title": "Input validation should exist",
        "severity": CRITICAL,
        "type": BOOLEAN,
        "json_path": "security.input_validation",
        "expected": True,
        "recommendation": "Validate all incoming user input.",
    },

    {
        "id": "SEC_015",
        "category": SECURITY,
        "principle": "Application Security",
        "title": "CORS should be configured",
        "severity": MEDIUM,
        "type": BOOLEAN,
        "json_path": "security.cors",
        "expected": True,
        "recommendation": "Configure CORS securely.",
    },

    {
        "id": "SEC_016",
        "category": SECURITY,
        "principle": "Application Security",
        "title": "Security headers should be enabled",
        "severity": MEDIUM,
        "type": BOOLEAN,
        "json_path": "security.security_headers",
        "expected": True,
        "recommendation": "Enable standard HTTP security headers.",
    },

    {
        "id": "SEC_017",
        "category": SECURITY,
        "principle": "Secrets Management",
        "title": "Secrets should be managed securely",
        "severity": CRITICAL,
        "type": BOOLEAN,
        "json_path": "security.secret_management",
        "expected": True,
        "recommendation": "Store secrets using a secure secret management solution.",
    },

    {
        "id": "SEC_018",
        "category": SECURITY,
        "principle": "Secrets Management",
        "title": "Secrets should not be stored in application code",
        "severity": HIGH,
        "type": BOOLEAN,
        "json_path": "security.secret_management",
        "expected": True,
        "recommendation": "Externalize secrets from application code.",
    },

    {
        "id": "SEC_019",
        "category": SECURITY,
        "principle": "Secrets Management",
        "title": "Default credentials should not be used",
        "severity": HIGH,
        "type": BOOLEAN,
        "json_path": "security.default_credentials",
        "expected": False,
        "recommendation": "Replace all default credentials before deployment.",
    },

    {
        "id": "SEC_020",
        "category": SECURITY,
        "principle": "Secrets Management",
        "title": "Security configuration should be centrally managed",
        "severity": MEDIUM,
        "type": BOOLEAN,
        "json_path": "security.secret_management",
        "expected": True,
        "recommendation": "Manage security configuration centrally.",
    },
        # ======================================================
    # RELIABILITY
    # ======================================================

    {
        "id": "REL_001",
        "category": RELIABILITY,
        "principle": "High Availability",
        "title": "Critical services should have redundant instances",
        "severity": CRITICAL,
        "type": INTEGER,
        "json_path": "services[].instances",
        "expected": 2,
        "recommendation": "Deploy multiple instances of every critical service.",
    },

    {
        "id": "REL_002",
        "category": RELIABILITY,
        "principle": "High Availability",
        "title": "Databases should support high availability",
        "severity": CRITICAL,
        "type": BOOLEAN,
        "json_path": "databases[].replication",
        "expected": True,
        "recommendation": "Enable database replication or clustering.",
    },

    {
        "id": "REL_003",
        "category": RELIABILITY,
        "principle": "High Availability",
        "title": "Critical services should avoid single points of failure",
        "severity": HIGH,
        "type": INTEGER,
        "json_path": "services[].instances",
        "expected": 2,
        "recommendation": "Eliminate single points of failure from critical services.",
    },

    {
        "id": "REL_004",
        "category": RELIABILITY,
        "principle": "High Availability",
        "title": "Health checks should be configured",
        "severity": MEDIUM,
        "type": BOOLEAN,
        "json_path": "load_balancer.health_checks",
        "expected": True,
        "recommendation": "Configure health checks for all critical services.",
    },

    {
        "id": "REL_005",
        "category": RELIABILITY,
        "principle": "Fault Tolerance",
        "title": "Retry mechanism should exist",
        "severity": HIGH,
        "type": BOOLEAN,
        "json_path": "resilience.retry_enabled",
        "expected": True,
        "recommendation": "Enable retry mechanisms for recoverable failures.",
    },

    {
        "id": "REL_006",
        "category": RELIABILITY,
        "principle": "Fault Tolerance",
        "title": "Timeouts should be configured",
        "severity": HIGH,
        "type": BOOLEAN,
        "json_path": "resilience.timeouts",
        "expected": True,
        "recommendation": "Configure request timeouts.",
    },

    {
        "id": "REL_007",
        "category": RELIABILITY,
        "principle": "Fault Tolerance",
        "title": "Circuit breaker should exist",
        "severity": MEDIUM,
        "type": BOOLEAN,
        "json_path": "resilience.circuit_breaker",
        "expected": True,
        "recommendation": "Use circuit breakers to isolate failures.",
    },

    {
        "id": "REL_008",
        "category": RELIABILITY,
        "principle": "Fault Tolerance",
        "title": "Graceful degradation should be supported",
        "severity": MEDIUM,
        "type": BOOLEAN,
        "json_path": "resilience.graceful_degradation",
        "expected": True,
        "recommendation": "Allow degraded operation during failures.",
    },

    {
        "id": "REL_009",
        "category": RELIABILITY,
        "principle": "Disaster Recovery",
        "title": "Backup strategy should exist",
        "severity": CRITICAL,
        "type": BOOLEAN,
        "json_path": "backup.enabled",
        "expected": True,
        "recommendation": "Enable regular backups.",
    },

    {
        "id": "REL_010",
        "category": RELIABILITY,
        "principle": "Disaster Recovery",
        "title": "Restore procedure should be tested",
        "severity": HIGH,
        "type": BOOLEAN,
        "json_path": "backup.restore_tested",
        "expected": True,
        "recommendation": "Regularly test backup restoration.",
    },

    {
        "id": "REL_011",
        "category": RELIABILITY,
        "principle": "Disaster Recovery",
        "title": "Recovery objectives should be defined",
        "severity": MEDIUM,
        "type": BOOLEAN,
        "json_path": "backup.rto_rpo_defined",
        "expected": True,
        "recommendation": "Define RTO and RPO objectives.",
    },

    {
        "id": "REL_012",
        "category": RELIABILITY,
        "principle": "Disaster Recovery",
        "title": "Disaster recovery process should be documented",
        "severity": MEDIUM,
        "type": BOOLEAN,
        "json_path": "backup.dr_documented",
        "expected": True,
        "recommendation": "Document disaster recovery procedures.",
    },

    {
        "id": "REL_013",
        "category": RELIABILITY,
        "principle": "Observability",
        "title": "Centralized logging should exist",
        "severity": HIGH,
        "type": BOOLEAN,
        "json_path": "monitoring.centralized_logging",
        "expected": True,
        "recommendation": "Use centralized log management.",
    },

    {
        "id": "REL_014",
        "category": RELIABILITY,
        "principle": "Observability",
        "title": "Monitoring should exist",
        "severity": HIGH,
        "type": BOOLEAN,
        "json_path": "monitoring.enabled",
        "expected": True,
        "recommendation": "Monitor all critical system components.",
    },

    {
        "id": "REL_015",
        "category": RELIABILITY,
        "principle": "Observability",
        "title": "Alerting should be configured",
        "severity": MEDIUM,
        "type": BOOLEAN,
        "json_path": "monitoring.alerting",
        "expected": True,
        "recommendation": "Configure alerts for critical failures.",
    },

    {
        "id": "REL_016",
        "category": RELIABILITY,
        "principle": "Observability",
        "title": "Health status endpoint should exist",
        "severity": MEDIUM,
        "type": BOOLEAN,
        "json_path": "monitoring.status_endpoint",
        "expected": True,
        "recommendation": "Provide service health endpoints.",
    },

    {
        "id": "REL_017",
        "category": RELIABILITY,
        "principle": "Resilient Deployment",
        "title": "Deployment should minimize downtime",
        "severity": MEDIUM,
        "type": BOOLEAN,
        "json_path": "deployment.zero_downtime",
        "expected": True,
        "recommendation": "Adopt zero-downtime deployment strategies.",
    },

    {
        "id": "REL_018",
        "category": RELIABILITY,
        "principle": "Resilient Deployment",
        "title": "Rollback mechanism should exist",
        "severity": HIGH,
        "type": BOOLEAN,
        "json_path": "deployment.rollback",
        "expected": True,
        "recommendation": "Implement deployment rollback capability.",
    },

    {
        "id": "REL_019",
        "category": RELIABILITY,
        "principle": "Resilient Deployment",
        "title": "Safe database migration strategy should exist",
        "severity": MEDIUM,
        "type": BOOLEAN,
        "json_path": "deployment.safe_db_migration",
        "expected": True,
        "recommendation": "Ensure schema migrations are backward compatible.",
    },

    {
        "id": "REL_020",
        "category": RELIABILITY,
        "principle": "Resilient Deployment",
        "title": "Configuration changes should not require rebuilds",
        "severity": LOW,
        "type": BOOLEAN,
        "json_path": "configuration.externalized",
        "expected": True,
        "recommendation": "Externalize configuration from application code.",
    },
        # ======================================================
    # PERFORMANCE
    # ======================================================

    {
        "id": "PER_001",
        "category": PERFORMANCE,
        "principle": "Response Optimization",
        "title": "Response caching should be used where appropriate",
        "severity": HIGH,
        "type": BOOLEAN,
        "json_path": "cache.enabled",
        "expected": True,
        "recommendation": "Enable response caching to reduce latency.",
    },

    {
        "id": "PER_002",
        "category": PERFORMANCE,
        "principle": "Response Optimization",
        "title": "API responses should support pagination",
        "severity": HIGH,
        "type": BOOLEAN,
        "json_path": "api.pagination",
        "expected": True,
        "recommendation": "Implement pagination for large result sets.",
    },

    {
        "id": "PER_003",
        "category": PERFORMANCE,
        "principle": "Response Optimization",
        "title": "Response compression should be enabled",
        "severity": MEDIUM,
        "type": BOOLEAN,
        "json_path": "api.compression",
        "expected": True,
        "recommendation": "Enable HTTP response compression.",
    },

    {
        "id": "PER_004",
        "category": PERFORMANCE,
        "principle": "Response Optimization",
        "title": "Long-running requests should be asynchronous",
        "severity": MEDIUM,
        "type": BOOLEAN,
        "json_path": "services[].async_processing",
        "expected": True,
        "recommendation": "Move long-running operations to background workers.",
    },

    {
        "id": "PER_005",
        "category": PERFORMANCE,
        "principle": "Database Optimization",
        "title": "Frequently queried fields should be indexed",
        "severity": CRITICAL,
        "type": BOOLEAN,
        "json_path": "databases[].indexes",
        "expected": True,
        "recommendation": "Create indexes on frequently queried fields.",
    },

    {
        "id": "PER_006",
        "category": PERFORMANCE,
        "principle": "Database Optimization",
        "title": "Database connection pooling should be configured",
        "severity": HIGH,
        "type": BOOLEAN,
        "json_path": "databases[].connection_pooling",
        "expected": True,
        "recommendation": "Enable database connection pooling.",
    },

    {
        "id": "PER_007",
        "category": PERFORMANCE,
        "principle": "Database Optimization",
        "title": "Database queries should be optimized",
        "severity": MEDIUM,
        "type": BOOLEAN,
        "json_path": "databases[].indexes",
        "expected": True,
        "recommendation": "Optimize expensive database queries.",
    },

    {
        "id": "PER_008",
        "category": PERFORMANCE,
        "principle": "Database Optimization",
        "title": "Read-heavy workloads should minimize database access",
        "severity": HIGH,
        "type": BOOLEAN,
        "json_path": "cache.enabled",
        "expected": True,
        "recommendation": "Reduce repeated database reads using caching.",
    },

    {
        "id": "PER_009",
        "category": PERFORMANCE,
        "principle": "Compute Efficiency",
        "title": "Background processing should be used",
        "severity": HIGH,
        "type": BOOLEAN,
        "json_path": "services[].async_processing",
        "expected": True,
        "recommendation": "Move CPU intensive tasks to background workers.",
    },

    {
        "id": "PER_010",
        "category": PERFORMANCE,
        "principle": "Compute Efficiency",
        "title": "Compute resources should support workload scaling",
        "severity": MEDIUM,
        "type": INTEGER,
        "json_path": "services[].instances",
        "expected": 2,
        "recommendation": "Provision scalable compute resources.",
    },

    {
        "id": "PER_011",
        "category": PERFORMANCE,
        "principle": "Compute Efficiency",
        "title": "Heavy workloads should be isolated",
        "severity": MEDIUM,
        "type": BOOLEAN,
        "json_path": "services[].async_processing",
        "expected": True,
        "recommendation": "Separate heavy workloads from user-facing services.",
    },

    {
        "id": "PER_012",
        "category": PERFORMANCE,
        "principle": "Compute Efficiency",
        "title": "Resource contention should be minimized",
        "severity": MEDIUM,
        "type": INTEGER,
        "json_path": "services[].instances",
        "expected": 2,
        "recommendation": "Distribute workloads across multiple instances.",
    },

    {
        "id": "PER_013",
        "category": PERFORMANCE,
        "principle": "Network Efficiency",
        "title": "Static content should use caching",
        "severity": MEDIUM,
        "type": BOOLEAN,
        "json_path": "cache.enabled",
        "expected": True,
        "recommendation": "Serve static assets through caching or CDN.",
    },

    {
        "id": "PER_014",
        "category": PERFORMANCE,
        "principle": "Network Efficiency",
        "title": "Network hops should be minimized",
        "severity": MEDIUM,
        "type": BOOLEAN,
        "json_path": "architecture.layered_design",
        "expected": True,
        "recommendation": "Avoid unnecessary service hops.",
    },

    {
        "id": "PER_015",
        "category": PERFORMANCE,
        "principle": "Network Efficiency",
        "title": "Payload sizes should be optimized",
        "severity": MEDIUM,
        "type": BOOLEAN,
        "json_path": "api.compression",
        "expected": True,
        "recommendation": "Reduce request and response payload sizes.",
    },

    {
        "id": "PER_016",
        "category": PERFORMANCE,
        "principle": "Network Efficiency",
        "title": "Network latency should be minimized",
        "severity": HIGH,
        "type": BOOLEAN,
        "json_path": "load_balancer.enabled",
        "expected": True,
        "recommendation": "Optimize request routing and network latency.",
    },

    {
        "id": "PER_017",
        "category": PERFORMANCE,
        "principle": "Resource Management",
        "title": "CPU and memory utilization should be monitored",
        "severity": MEDIUM,
        "type": BOOLEAN,
        "json_path": "monitoring.enabled",
        "expected": True,
        "recommendation": "Monitor CPU and memory usage continuously.",
    },

    {
        "id": "PER_018",
        "category": PERFORMANCE,
        "principle": "Resource Management",
        "title": "Resource limits should be defined",
        "severity": MEDIUM,
        "type": BOOLEAN,
        "json_path": "monitoring.enabled",
        "expected": True,
        "recommendation": "Define CPU and memory limits for workloads.",
    },

    {
        "id": "PER_019",
        "category": PERFORMANCE,
        "principle": "Resource Management",
        "title": "Idle resource consumption should be minimized",
        "severity": LOW,
        "type": BOOLEAN,
        "json_path": "monitoring.enabled",
        "expected": True,
        "recommendation": "Identify and eliminate idle resource usage.",
    },

    {
        "id": "PER_020",
        "category": PERFORMANCE,
        "principle": "Resource Management",
        "title": "Performance bottlenecks should be observable",
        "severity": HIGH,
        "type": BOOLEAN,
        "json_path": "monitoring.enabled",
        "expected": True,
        "recommendation": "Monitor performance metrics to identify bottlenecks.",
    },
        # ======================================================
    # MAINTAINABILITY
    # ======================================================

    {
        "id": "MAI_001",
        "category": MAINTAINABILITY,
        "principle": "Architecture & Design",
        "title": "System should follow a layered or modular architecture",
        "severity": HIGH,
        "type": BOOLEAN,
        "json_path": "architecture.layered_design",
        "expected": True,
        "recommendation": "Adopt a layered or modular architecture.",
    },

    {
        "id": "MAI_002",
        "category": MAINTAINABILITY,
        "principle": "Architecture & Design",
        "title": "Components should have clear separation of responsibilities",
        "severity": HIGH,
        "type": BOOLEAN,
        "json_path": "architecture.separation_of_concerns",
        "expected": True,
        "recommendation": "Separate business logic, infrastructure, and presentation responsibilities.",
    },

    {
        "id": "MAI_003",
        "category": MAINTAINABILITY,
        "principle": "Architecture & Design",
        "title": "Services should expose well-defined interfaces",
        "severity": MEDIUM,
        "type": BOOLEAN,
        "json_path": "architecture.interface_definition",
        "expected": True,
        "recommendation": "Define clear contracts between services.",
    },

    {
        "id": "MAI_004",
        "category": MAINTAINABILITY,
        "principle": "Architecture & Design",
        "title": "Components should avoid excessive coupling",
        "severity": CRITICAL,
        "type": BOOLEAN,
        "json_path": "architecture.loose_coupling",
        "expected": True,
        "recommendation": "Reduce coupling between modules and services.",
    },

    {
        "id": "MAI_005",
        "category": MAINTAINABILITY,
        "principle": "Testing",
        "title": "Unit testing strategy should exist",
        "severity": HIGH,
        "type": BOOLEAN,
        "json_path": "testing.unit_tests",
        "expected": True,
        "recommendation": "Implement unit tests for business logic.",
    },

    {
        "id": "MAI_006",
        "category": MAINTAINABILITY,
        "principle": "Testing",
        "title": "Integration testing strategy should exist",
        "severity": HIGH,
        "type": BOOLEAN,
        "json_path": "testing.integration_tests",
        "expected": True,
        "recommendation": "Validate interactions between system components.",
    },

    {
        "id": "MAI_007",
        "category": MAINTAINABILITY,
        "principle": "Testing",
        "title": "API testing strategy should exist",
        "severity": MEDIUM,
        "type": BOOLEAN,
        "json_path": "testing.api_tests",
        "expected": True,
        "recommendation": "Create automated API tests.",
    },

    {
        "id": "MAI_008",
        "category": MAINTAINABILITY,
        "principle": "Testing",
        "title": "Critical components should be independently testable",
        "severity": HIGH,
        "type": BOOLEAN,
        "json_path": "testing.component_testability",
        "expected": True,
        "recommendation": "Design components for independent testing.",
    },

    {
        "id": "MAI_009",
        "category": MAINTAINABILITY,
        "principle": "Documentation",
        "title": "API documentation should exist",
        "severity": HIGH,
        "type": BOOLEAN,
        "json_path": "documentation.api_docs",
        "expected": True,
        "recommendation": "Maintain accurate API documentation.",
    },

    {
        "id": "MAI_010",
        "category": MAINTAINABILITY,
        "principle": "Documentation",
        "title": "Architecture documentation should exist",
        "severity": HIGH,
        "type": BOOLEAN,
        "json_path": "documentation.architecture_docs",
        "expected": True,
        "recommendation": "Document architecture decisions and diagrams.",
    },

    {
        "id": "MAI_011",
        "category": MAINTAINABILITY,
        "principle": "Documentation",
        "title": "Deployment documentation should exist",
        "severity": MEDIUM,
        "type": BOOLEAN,
        "json_path": "documentation.deployment_docs",
        "expected": True,
        "recommendation": "Document deployment procedures.",
    },

    {
        "id": "MAI_012",
        "category": MAINTAINABILITY,
        "principle": "Documentation",
        "title": "Operational procedures should be documented",
        "severity": MEDIUM,
        "type": BOOLEAN,
        "json_path": "documentation.operations_docs",
        "expected": True,
        "recommendation": "Document operational and maintenance procedures.",
    },

    {
        "id": "MAI_013",
        "category": MAINTAINABILITY,
        "principle": "Configuration Management",
        "title": "Configuration should be externalized",
        "severity": CRITICAL,
        "type": BOOLEAN,
        "json_path": "configuration.externalized",
        "expected": True,
        "recommendation": "Move configuration outside application code.",
    },

    {
        "id": "MAI_014",
        "category": MAINTAINABILITY,
        "principle": "Configuration Management",
        "title": "Environment-specific configuration should be supported",
        "severity": HIGH,
        "type": BOOLEAN,
        "json_path": "configuration.environment_support",
        "expected": True,
        "recommendation": "Support separate configurations for each environment.",
    },

    {
        "id": "MAI_015",
        "category": MAINTAINABILITY,
        "principle": "Configuration Management",
        "title": "Configuration should be centrally managed",
        "severity": MEDIUM,
        "type": BOOLEAN,
        "json_path": "configuration.centralized",
        "expected": True,
        "recommendation": "Use centralized configuration management.",
    },

    {
        "id": "MAI_016",
        "category": MAINTAINABILITY,
        "principle": "Configuration Management",
        "title": "Hardcoded environment values should be avoided",
        "severity": HIGH,
        "type": BOOLEAN,
        "json_path": "configuration.no_hardcoded_values",
        "expected": True,
        "recommendation": "Avoid hardcoding environment-specific values.",
    },

    {
        "id": "MAI_017",
        "category": MAINTAINABILITY,
        "principle": "Delivery & Operations",
        "title": "CI/CD pipeline should exist",
        "severity": HIGH,
        "type": BOOLEAN,
        "json_path": "deployment.cicd",
        "expected": True,
        "recommendation": "Adopt an automated CI/CD pipeline.",
    },

    {
        "id": "MAI_018",
        "category": MAINTAINABILITY,
        "principle": "Delivery & Operations",
        "title": "API versioning strategy should exist",
        "severity": MEDIUM,
        "type": BOOLEAN,
        "json_path": "api.versioning",
        "expected": True,
        "recommendation": "Version APIs to support backward compatibility.",
    },

    {
        "id": "MAI_019",
        "category": MAINTAINABILITY,
        "principle": "Delivery & Operations",
        "title": "Dependency management strategy should exist",
        "severity": MEDIUM,
        "type": BOOLEAN,
        "json_path": "deployment.cicd",
        "expected": True,
        "recommendation": "Manage and update dependencies systematically.",
    },

    {
        "id": "MAI_020",
        "category": MAINTAINABILITY,
        "principle": "Delivery & Operations",
        "title": "Deployment process should support repeatable releases",
        "severity": HIGH,
        "type": BOOLEAN,
        "json_path": "deployment.repeatable_releases",
        "expected": True,
        "recommendation": "Automate deployments to ensure repeatable releases.",
    },


]