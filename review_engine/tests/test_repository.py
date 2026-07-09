from django.contrib.auth.models import User
from django.test import TestCase

from review_engine.repository.review_repository import ReviewRepository
from review_engine.tests.test_data import get_valid_architecture


class RepositoryTests(TestCase):

    def setUp(self):

        self.repository = ReviewRepository()

        self.user = User.objects.create_user(
            username="prasad",
            password="Password123",
        )

    def test_save_review(self):

        review = self.repository.save_review(
            user=self.user,
            architecture=get_valid_architecture(),
            review_result={"overall_score": 100},
        )

        self.assertEqual(
            review["user_id"],
            self.user.id,
        )

        self.assertEqual(
            review["username"],
            self.user.username,
        )

    def test_get_all_reviews(self):

        self.repository.save_review(
            user=self.user,
            architecture=get_valid_architecture(),
            review_result={"overall_score": 100},
        )

        reviews = self.repository.get_all_reviews(
            self.user
        )

        self.assertGreaterEqual(
            len(reviews),
            1,
        )