from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase


class AuthenticationTests(APITestCase):

    # =====================================================
    # Register Success
    # =====================================================

    def test_register_success(self):

        response = self.client.post(
            reverse("register"),
            {
                "username": "prasad",
                "email": "prasad@test.com",
                "password": "Password123",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

        self.assertTrue(
            User.objects.filter(
                username="prasad"
            ).exists()
        )

    # =====================================================
    # Duplicate Username
    # =====================================================

    def test_duplicate_username(self):

        User.objects.create_user(
            username="prasad",
            email="old@test.com",
            password="Password123",
        )

        response = self.client.post(
            reverse("register"),
            {
                "username": "prasad",
                "email": "new@test.com",
                "password": "Password123",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )

    # =====================================================
    # Duplicate Email
    # =====================================================

    def test_duplicate_email(self):

        User.objects.create_user(
            username="user1",
            email="prasad@test.com",
            password="Password123",
        )

        response = self.client.post(
            reverse("register"),
            {
                "username": "user2",
                "email": "prasad@test.com",
                "password": "Password123",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )

    # =====================================================
    # Login Success
    # =====================================================

    def test_login_success(self):

        User.objects.create_user(
            username="prasad",
            password="Password123",
        )

        response = self.client.post(
            reverse("login"),
            {
                "username": "prasad",
                "password": "Password123",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertIn(
            "access",
            response.data,
        )

        self.assertIn(
            "refresh",
            response.data,
        )

    # =====================================================
    # Wrong Password
    # =====================================================

    def test_wrong_password(self):

        User.objects.create_user(
            username="prasad",
            password="Password123",
        )

        response = self.client.post(
            reverse("login"),
            {
                "username": "prasad",
                "password": "WrongPassword",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED,
        )

    # =====================================================
    # Wrong Username
    # =====================================================

    def test_wrong_username(self):

        response = self.client.post(
            reverse("login"),
            {
                "username": "unknown",
                "password": "Password123",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED,
        )
    # =====================================================
# Protected API Without Token
# =====================================================

    def test_protected_api_without_token(self):

        response = self.client.get(
        reverse("review-list")
    )

        self.assertEqual(
        response.status_code,
        status.HTTP_401_UNAUTHORIZED,
    )


# =====================================================
# Protected API With Token
# =====================================================

    def test_protected_api_with_token(self):

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

        response = self.client.get(
        reverse("review-list")
    )

        self.assertEqual(
        response.status_code,
        status.HTTP_200_OK,
    )


# =====================================================
# Refresh Token
# =====================================================

    def test_refresh_token(self):

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

        refresh = login.data["refresh"]

        response = self.client.post(
        reverse("refresh"),
        {
            "refresh": refresh,
        },
        format="json",
    )

        self.assertEqual(
        response.status_code,
        status.HTTP_200_OK,
    )

        self.assertIn(
        "access",
        response.data,
    )