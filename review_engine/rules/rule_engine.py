"""
Architecture Rule Engine

Coordinates execution of the Rule Book.

Responsibilities:
- Iterate over all rules
- Evaluate each rule
- Produce RuleResult

Does NOT:
- Calculate scores
- Perform business validation
"""

from review_engine.schemas.rule_constants import RULES
from review_engine.rules.rule_result import RuleResult
from review_engine.rules.evaluator import evaluate_rule


class RuleEngine:

    def __init__(self, architecture):

        self.architecture = architecture
        self.result = RuleResult()

    def evaluate(self):

        for rule in RULES:

            evaluate_rule(
                rule=rule,
                architecture=self.architecture,
                result=self.result,
            )

        return self.result