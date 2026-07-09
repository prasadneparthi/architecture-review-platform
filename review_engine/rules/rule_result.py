"""
Rule Result

Stores raw rule evaluation results.

Responsibilities:
- Store rule evaluation results
- Store rule violations

Does NOT:
- Calculate scores
- Generate strengths
- Generate weaknesses
- Generate recommendations
"""


class RuleResult:

    def __init__(self):

        self.rule_results = []
        self.violations = []

    def add_rule_result(
        self,
        rule_id,
        title,
        category,
        status,
        severity,
        score_change=0,
        recommendation=None,
    ):

        rule_result = {
            "rule_id": rule_id,
            "title": title,
            "category": category,
            "status": status,
            "severity": severity,
            "score_change": score_change,
        }

        if status == "FAIL":
            rule_result["recommendation"] = recommendation

        self.rule_results.append(rule_result)

    def add_violation(
        self,
        rule_id,
        category,
        severity,
    ):

        self.violations.append(
            {
                "rule_id": rule_id,
                "category": category,
                "severity": severity,
            }
        )

    def to_dict(self):

        return {
            "rule_results": self.rule_results,
            "violations": self.violations,
        }