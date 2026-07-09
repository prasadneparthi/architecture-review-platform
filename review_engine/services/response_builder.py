"""
Response Builder

Builds the final API response.
"""

from collections import defaultdict


class ResponseBuilder:

    def __init__(
        self,
        system_name,
        scores,
        rule_result,
    ):

        self.system_name = system_name
        self.scores = scores
        self.rule_result = rule_result

    def build(self):

        strengths = []
        weaknesses = []
        recommendations = []

        passed = defaultdict(int)
        failed = defaultdict(int)

        for rule in self.rule_result.rule_results:

            category = rule["category"]

            if rule["status"] == "PASS":

                passed[category] += 1

            elif rule["status"] == "FAIL":

                failed[category] += 1

                recommendations.append(
                    {
                        "rule_id": rule["rule_id"],
                        "title": rule["title"],
                        "category": rule["category"],
                        "severity": rule["severity"],
                        "description": rule.get(
                            "recommendation"
                        ),
                    }
                )

        # -------------------------------------
        # Strengths
        # -------------------------------------

        for category in passed:

            if failed.get(category, 0) == 0:

                strengths.append(
                    f"{category} practices are well implemented."
                )

        # -------------------------------------
        # Weaknesses
        # -------------------------------------

        for category in failed:

            if failed[category] > 0:

                weaknesses.append(
                    f"{category} requires improvement."
                )

        return {

            "system_name": self.system_name,

            "overall_score": self.scores[
                "overall_score"
            ],

            "category_scores": self.scores[
                "category_scores"
            ],

            "rule_results": self.rule_result.rule_results,

            "strengths": strengths,

            "weaknesses": weaknesses,

            "recommendations": recommendations,

            "violations": self.rule_result.violations,

            "llm_analysis": None,
        }