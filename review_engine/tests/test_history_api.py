from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from review_engine.repository.review_repository import ReviewRepository
from review_engine.tests.test_data import get_valid_architecture


class HistoryAPITests(APITestCase):

    def setUp(self):

        self.repository = ReviewRepository()

        self.user = User.objects.create_user(
            username="prasad",
            password="Password123",
        )

        login = self.client.post(
            reverse("login"),
            {
                "username": "prasad",
                "password": "Password123",
            },
            format="json",
        )

        token = login.data["access"]

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {token}"
        )

        self.repository.save_review(
            user=self.user,
            architecture=get_valid_architecture(),
            review_result={"overall_score": 100},
        )

    def test_get_reviews(self):

        response = self.client.get(
            reverse("review-list")
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertIsInstance(
            response.data,
            list,
        )