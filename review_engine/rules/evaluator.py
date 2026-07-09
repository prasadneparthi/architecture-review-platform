"""
Generic Rule Evaluator

Evaluates a single rule from the Rule Book.

Responsibilities:
- Compare actual value with expected value
- Determine PASS / FAIL / NOT_EVALUATED
- Populate RuleResult

Does NOT:
- Resolve JSON paths
- Calculate scores
"""

from review_engine.schemas.rule_constants import (
    BOOLEAN,
    INTEGER,
    EXISTS,
)

from review_engine.rules.rule_utils import get_value


PASS = "PASS"
FAIL = "FAIL"
NOT_EVALUATED = "NOT_EVALUATED"


def evaluate_rule(rule: dict, architecture: dict, result):
    """
    Evaluate a single rule.
    """

    actual_value = get_value(
        architecture,
        rule["json_path"]
    )

    status = determine_status(
        actual_value,
        rule
    )

    result.add_rule_result(
        rule_id=rule["id"],
        title=rule["title"],
        category=rule["category"],
        status=status,
        severity=rule["severity"],
        score_change=0,
        recommendation=(
            rule["recommendation"]
            if status == FAIL
            else None
        ),
    )

    if status == FAIL:

        result.add_violation(
            rule_id=rule["id"],
            category=rule["category"],
            severity=rule["severity"],
        )


def determine_status(value, rule):
    """
    Determine whether a rule passes.
    """

    rule_type = rule["type"]
    expected = rule["expected"]

    if value is None:
        return NOT_EVALUATED

    if rule_type == BOOLEAN:
        return evaluate_boolean(
            value,
            expected
        )

    if rule_type == INTEGER:
        return evaluate_integer(
            value,
            expected
        )

    if rule_type == EXISTS:
        return evaluate_exists(
            value
        )

    return NOT_EVALUATED


def evaluate_boolean(value, expected):

    if isinstance(value, list):

        return (
            PASS
            if all(v == expected for v in value)
            else FAIL
        )

    return PASS if value == expected else FAIL


def evaluate_integer(value, expected):

    if isinstance(value, list):

        return (
            PASS
            if all(v >= expected for v in value)
            else FAIL
        )

    return PASS if value >= expected else FAIL


def evaluate_exists(value):

    if isinstance(value, list):

        return (
            PASS
            if all(v is not None for v in value)
            else FAIL
        )

    return PASS if value is not None else FAIL