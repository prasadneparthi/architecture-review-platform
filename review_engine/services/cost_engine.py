"""
Architecture Cost Engine

Calculates architecture cost efficiency.

Responsibilities
----------------
- Calculate cost score
- Identify major cost drivers
- Generate optimization suggestions

Does NOT
--------
- Estimate cloud pricing
- Recommend removing infrastructure
"""

from review_engine.config.cost_constants import (
    MAX_COST_SCORE,
    MIN_COST_SCORE,
    SERVICE_WEIGHT,
    INSTANCE_WEIGHT,
    LOAD_BALANCER_WEIGHT,
    CACHE_WEIGHT,
    MESSAGE_QUEUE_WEIGHT,
    DATABASE_WEIGHT,
    REPLICATION_WEIGHT,
    READ_REPLICA_WEIGHT,
    SHARDING_WEIGHT,
    MONITORING_WEIGHT,
    BACKUP_WEIGHT,
    DR_WEIGHT,
    VERY_LOW_COST,
    LOW_COST,
    MEDIUM_COST,
    HIGH_COST,
    VERY_LOW,
    LOW,
    MEDIUM,
    HIGH,
    VERY_HIGH,
)


class CostEngine:

    def __init__(self, architecture):

        self.architecture = architecture

        self.score = MAX_COST_SCORE

        self.cost_drivers = []

        self.optimization_suggestions = []

    # =====================================================
    # Main
    # =====================================================

    def analyze(self):

        self._evaluate_services()

        self._evaluate_database()

        self._evaluate_load_balancer()

        self._evaluate_cache()

        self._evaluate_message_queue()

        self._evaluate_monitoring()

        self._evaluate_backup()

        self.score = max(
            MIN_COST_SCORE,
            self.score,
        )

        return {

            "cost_score": self.score,

            "cost_rating": self._get_rating(),

            "major_cost_drivers": self.cost_drivers,

            "optimization_suggestions":
                self.optimization_suggestions,
        }

    # =====================================================
    # Services
    # =====================================================

    def _evaluate_services(self):

        services = self.architecture["services"]

        self.score -= len(services) * SERVICE_WEIGHT

        if len(services) > 1:

            self.cost_drivers.append(
                "Multiple application services"
            )

        total_instances = sum(
            service["instances"]
            for service in services
        )

        self.score -= (
            total_instances * INSTANCE_WEIGHT
        )

        if total_instances > len(services):

            self.cost_drivers.append(
                "Multiple service instances"
            )

            self.optimization_suggestions.append(
                "Consider autoscaling instead of fixed service instances."
            )

    # =====================================================
    # Database
    # =====================================================

    def _evaluate_database(self):

        databases = self.architecture["databases"]

        for db in databases:

            self.score -= DATABASE_WEIGHT

            if db["replication"]:

                self.score -= REPLICATION_WEIGHT

                self.cost_drivers.append(
                    "Database replication"
                )

                self.optimization_suggestions.append(
                    "Review whether database replication matches your availability requirements."
                )

            if db["read_replicas"]:

                self.score -= READ_REPLICA_WEIGHT

                self.cost_drivers.append(
                    "Read replicas"
                )

            if db["sharding"]:

                self.score -= SHARDING_WEIGHT

                self.cost_drivers.append(
                    "Database sharding"
                )

                self.optimization_suggestions.append(
                    "Review whether sharding is required for the current workload."
                )

    # =====================================================
    # Load Balancer
    # =====================================================

    def _evaluate_load_balancer(self):

        lb = self.architecture["load_balancer"]

        if lb["enabled"]:

            self.score -= LOAD_BALANCER_WEIGHT

            self.cost_drivers.append(
                "Load balancer"
            )

    # =====================================================
    # Cache
    # =====================================================

    def _evaluate_cache(self):

        cache = self.architecture["cache"]

        if cache["enabled"]:

            self.score -= CACHE_WEIGHT

            self.cost_drivers.append(
                "Distributed cache"
            )

            self.optimization_suggestions.append(
                "Evaluate whether distributed caching provides measurable benefit for the expected workload."
            )

    # =====================================================
    # Queue
    # =====================================================

    def _evaluate_message_queue(self):

        queue = self.architecture["message_queue"]

        if queue["enabled"]:

            self.score -= MESSAGE_QUEUE_WEIGHT

            self.cost_drivers.append(
                "Message queue"
            )

            self.optimization_suggestions.append(
                "Review whether asynchronous messaging is required for current business requirements."
            )

    # =====================================================
    # Monitoring
    # =====================================================

    def _evaluate_monitoring(self):

        monitoring = self.architecture["monitoring"]

        if monitoring["enabled"]:

            self.score -= MONITORING_WEIGHT

            self.cost_drivers.append(
                "Monitoring infrastructure"
            )

    # =====================================================
    # Backup
    # =====================================================

    def _evaluate_backup(self):

        backup = self.architecture["backup"]

        if backup["enabled"]:

            self.score -= BACKUP_WEIGHT

            self.cost_drivers.append(
                "Backup infrastructure"
            )

        if backup["dr_documented"]:

            self.score -= DR_WEIGHT

            self.cost_drivers.append(
                "Disaster recovery planning"
            )

    # =====================================================
    # Rating
    # =====================================================

    def _get_rating(self):

        if self.score >= VERY_LOW_COST:
            return VERY_LOW

        if self.score >= LOW_COST:
            return LOW

        if self.score >= MEDIUM_COST:
            return MEDIUM

        if self.score >= HIGH_COST:
            return HIGH

        return VERY_HIGH