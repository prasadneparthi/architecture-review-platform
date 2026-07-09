"""
Architecture Score Engine

Calculates category scores and overall score
from Rule Engine results.

Responsibilities:
- Calculate category scores
- Calculate overall score
- Update score_change for failed rules

Does NOT:
- Evaluate rules
- Generate recommendations
"""

from collections import defaultdict

from review_engine.config.constants import (
    MAX_SCORE,
    MIN_SCORE,
)

from review_engine.schemas.rule_constants import (
    CRITICAL,
    HIGH,
    MEDIUM,
    LOW,
)

# Score deduction based on rule severity
SEVERITY_DEDUCTION = {
    CRITICAL: 10,
    HIGH: 6,
    MEDIUM: 3,
    LOW: 1,
}


class ScoreEngine:

    def __init__(self, rule_result):
        self.rule_result = rule_result

    def calculate(self):
        """
        Calculate category and overall scores.
        """

        category_scores = defaultdict(lambda: MAX_SCORE)

        # Process every evaluated rule
        for rule in self.rule_result.rule_results:

            if rule["status"] != "FAIL":
                continue

            deduction = SEVERITY_DEDUCTION.get(
                rule["severity"],
                0,
            )

            category = rule["category"]

            category_scores[category] -= deduction

            # Prevent negative scores
            if category_scores[category] < MIN_SCORE:
                category_scores[category] = MIN_SCORE

            # Store deduction in rule result
            rule["score_change"] = -deduction

        # Ensure every category exists
        categories = [
            "Scalability",
            "Security",
            "Reliability",
            "Performance",
            "Maintainability",
        ]

        for category in categories:
            category_scores.setdefault(category, MAX_SCORE)

        overall_score = round(
            sum(category_scores.values())
            / len(category_scores)
        )

        return {
            "overall_score": overall_score,

            "category_scores": {
                "scalability": category_scores["Scalability"],
                "security": category_scores["Security"],
                "reliability": category_scores["Reliability"],
                "performance": category_scores["Performance"],
                "maintainability": category_scores["Maintainability"],
            }
        }