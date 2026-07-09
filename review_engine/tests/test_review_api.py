from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from review_engine.tests.test_data import get_valid_architecture


class ReviewAPITests(APITestCase):

    def setUp(self):

        User.objects.create_user(
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

    def test_review_api(self):

        response = self.client.post(
            reverse("architecture-review"),
            get_valid_architecture(),
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertIn(
            "overall_score",
            response.data,
        )