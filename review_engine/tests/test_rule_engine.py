from django.test import TestCase

from review_engine.rules.rule_engine import RuleEngine

from review_engine.tests.test_data import (
    get_valid_architecture,
)


class RuleEngineTests(TestCase):

    # =====================================================
    # Perfect Architecture
    # =====================================================

    def test_perfect_architecture(self):

        result = RuleEngine(
            get_valid_architecture()
        ).evaluate()

        self.assertGreater(
            len(result.rule_results),
            0,
        )

        failed = [
            rule
            for rule in result.rule_results
            if rule["status"] == "FAIL"
        ]

        self.assertEqual(
            len(failed),
            0,
        )

        self.assertEqual(
            len(result.violations),
            0,
        )

    # =====================================================
    # Faulty Architecture
    # =====================================================

    def test_faulty_architecture(self):

        data = get_valid_architecture()

        data["cache"]["enabled"] = False
        data["security"]["https"] = False
        data["monitoring"]["enabled"] = False

        result = RuleEngine(
            data
        ).evaluate()

        failed = [
            rule
            for rule in result.rule_results
            if rule["status"] == "FAIL"
        ]

        self.assertGreater(
            len(failed),
            0,
        )

        self.assertGreater(
            len(result.violations),
            0,
        )

    # =====================================================
    # Violations Generated
    # =====================================================

    def test_violations_generated(self):

        data = get_valid_architecture()

        data["security"]["https"] = False

        result = RuleEngine(
            data
        ).evaluate()

        self.assertGreater(
            len(result.violations),
            0,
        )

    # =====================================================
    # Rule Results Generated
    # =====================================================

    def test_rule_results_generated(self):

        result = RuleEngine(
            get_valid_architecture()
        ).evaluate()

        self.assertGreater(
            len(result.rule_results),
            0,
        )

    # =====================================================
    # Rule Result Structure
    # =====================================================

    def test_rule_result_structure(self):

        result = RuleEngine(
            get_valid_architecture()
        ).evaluate()

        rule = result.rule_results[0]

        self.assertIn(
            "rule_id",
            rule,
        )

        self.assertIn(
            "title",
            rule,
        )

        self.assertIn(
            "category",
            rule,
        )

        self.assertIn(
            "status",
            rule,
        )

        self.assertIn(
            "severity",
            rule,
        )

        self.assertIn(
            "score_change",
            rule,
        )

    # =====================================================
    # to_dict()
    # =====================================================

    def test_to_dict(self):

        result = RuleEngine(
            get_valid_architecture()
        ).evaluate()

        data = result.to_dict()

        self.assertIn(
            "rule_results",
            data,
        )

        self.assertIn(
            "violations",
            data,
        )