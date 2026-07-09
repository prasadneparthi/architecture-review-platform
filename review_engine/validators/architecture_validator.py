"""
Architecture Business Validator

Performs business validations after serializer validation.

Responsibilities:
- Business validations
- Cross-object validations
- Dependency validations

Does NOT:
- Validate datatypes
- Validate required fields
- Calculate scores
"""

from typing import List

from review_engine.exceptions.custom_exceptions import (
    ArchitectureValidationError,
)


class ArchitectureValidator:

    def __init__(self, data: dict):
        self.data = data
        self.errors = []

    # ======================================================
    # Services
    # ======================================================

    def validate_services(self):

        services = self.data.get("services", [])

        if not services:
            self.errors.append({
                "field": "services",
                "message": "At least one service is required."
            })
            return

        names = set()

        for index, service in enumerate(services):

            name = service["name"]

            if name in names:
                self.errors.append({
                    "field": f"services[{index}].name",
                    "message": f"Duplicate service name '{name}'."
                })

            names.add(name)

            if service["instances"] < 1:
                self.errors.append({
                    "field": f"services[{index}].instances",
                    "message": f"Service '{name}' must have at least one instance."
                })

    # ======================================================
    # Databases
    # ======================================================

    def validate_databases(self):

        databases = self.data.get("databases", [])

        if not databases:
            self.errors.append({
                "field": "databases",
                "message": "At least one database is required."
            })

    # ======================================================
    # Cache
    # ======================================================

    def validate_cache(self):

        cache = self.data["cache"]

        if cache["enabled"] and not cache.get("type"):
            self.errors.append({
                "field": "cache.type",
                "message": "Cache type is required when cache is enabled."
            })

    # ======================================================
    # Message Queue
    # ======================================================

    def validate_message_queue(self):

        queue = self.data["message_queue"]

        if queue["enabled"] and not queue.get("type"):
            self.errors.append({
                "field": "message_queue.type",
                "message": "Message queue type is required when enabled."
            })

    # ======================================================
    # Security
    # ======================================================

    def validate_security(self):

        security = self.data["security"]

        if security["authentication"] and not security.get(
            "authentication_type"
        ):
            self.errors.append({
                "field": "security.authentication_type",
                "message": "Authentication type is required."
            })

        if security["authorization"] and not security.get(
            "authorization_model"
        ):
            self.errors.append({
                "field": "security.authorization_model",
                "message": "Authorization model is required."
            })

    # ======================================================
    # Backup
    # ======================================================

    def validate_backup(self):

        backup = self.data["backup"]

        if backup["restore_tested"] and not backup["enabled"]:
            self.errors.append({
                "field": "backup.enabled",
                "message": "Backup must be enabled before restore testing."
            })

    # ======================================================
    # Architecture
    # ======================================================

    def validate_architecture(self):

        architecture = self.data["architecture"]

        if (
            architecture["interface_definition"]
            and not architecture["layered_design"]
        ):
            self.errors.append({
                "field": "architecture.layered_design",
                "message": "Interface definition requires layered architecture."
            })

    # ======================================================
    # Main Validation
    # ======================================================

    def validate(self) -> List[dict]:

        self.validate_services()
        self.validate_databases()
        self.validate_cache()
        self.validate_message_queue()
        self.validate_security()
        self.validate_backup()
        self.validate_architecture()

        if self.errors:
            raise ArchitectureValidationError(self.errors)

        return []