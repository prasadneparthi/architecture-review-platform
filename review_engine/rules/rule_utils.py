"""
Rule Utility Functions

Provides helper functions for the Generic Rule Engine.

Responsibilities:
- Resolve JSON paths
- Extract values from architecture data

Does NOT:
- Evaluate rules
- Calculate scores
"""

from typing import Any


def get_value(data: Any, json_path: str):
    """
    Resolve a rule JSON path against the architecture.

    Examples
    --------
    "load_balancer.enabled"

    "cache.enabled"

    "security.https"

    "services[].instances"

    "databases[].replication"
    """

    parts = json_path.split(".")

    current = data

    for part in parts:

        # Handle list access (services[], databases[])
        if part.endswith("[]"):

            key = part[:-2]

            if isinstance(current, dict):
                current = current.get(key, [])
            else:
                return []

        else:

            # Current object is a list
            if isinstance(current, list):

                values = []

                for item in current:

                    if isinstance(item, dict):
                        values.append(item.get(part))

                return values

            # Current object is a dictionary
            elif isinstance(current, dict):

                current = current.get(part)

            else:
                return None

    return current