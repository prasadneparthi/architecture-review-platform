from django.test import TestCase

from review_engine.rules.rule_engine import RuleEngine
from review_engine.services.score_engine import ScoreEngine

from review_engine.tests.test_data import (
    get_valid_architecture,
)


class ScoreEngineTests(TestCase):

    def test_score_generation(self):

        rules = RuleEngine(
            get_valid_architecture()
        ).evaluate()

        scores = ScoreEngine(
            rules
        ).calculate()

        self.assertIn(
            "overall_score",
            scores,
        )

    def test_score_is_integer(self):

        rules = RuleEngine(
            get_valid_architecture()
        ).evaluate()

        scores = ScoreEngine(
            rules
        ).calculate()

        self.assertIsInstance(
            scores["overall_score"],
            int,
        )

    def test_score_between_0_and_100(self):

        rules = RuleEngine(
            get_valid_architecture()
        ).evaluate()

        scores = ScoreEngine(
            rules
        ).calculate()

        self.assertGreaterEqual(
            scores["overall_score"],
            0,
        )

        self.assertLessEqual(
            scores["overall_score"],
            100,
        )