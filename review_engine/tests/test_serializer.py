from django.test import TestCase

from review_engine.api.serializers import (
    ArchitectureSerializer,
)

from review_engine.tests.test_data import (
    get_valid_architecture,
)


class ArchitectureSerializerTests(TestCase):

    # =====================================================
    # Valid Input
    # =====================================================

    def test_valid_serializer(self):

        serializer = ArchitectureSerializer(
            data=get_valid_architecture()
        )
        valid = serializer.is_valid()
        
        self.assertTrue(
            valid
        )

    # =====================================================
    # Missing Required Field
    # =====================================================

    def test_missing_system_name(self):

        data = get_valid_architecture()

        del data["system_name"]

        serializer = ArchitectureSerializer(
            data=data
        )

        self.assertFalse(
            serializer.is_valid()
        )

        self.assertIn(
            "system_name",
            serializer.errors,
        )

    # =====================================================
    # Invalid Architecture Type
    # =====================================================

    def test_invalid_architecture_type(self):

        data = get_valid_architecture()

        data["architecture_type"] = "InvalidArchitecture"

        serializer = ArchitectureSerializer(
            data=data
        )

        self.assertFalse(
            serializer.is_valid()
        )

        self.assertIn(
            "architecture_type",
            serializer.errors,
        )

    # =====================================================
    # Invalid Datatype
    # =====================================================

    def test_invalid_instances_type(self):

        data = get_valid_architecture()

        data["services"][0]["instances"] = "two"

        serializer = ArchitectureSerializer(
            data=data
        )

        self.assertFalse(
            serializer.is_valid()
        )

        self.assertIn(
            "services",
            serializer.errors,
        )

    # =====================================================
    # Invalid Database Type
    # =====================================================

    def test_invalid_database_type(self):

        data = get_valid_architecture()

        data["databases"][0]["type"] = "InvalidDatabase"

        serializer = ArchitectureSerializer(
            data=data
        )

        self.assertFalse(
            serializer.is_valid()
        )

        self.assertIn(
            "databases",
            serializer.errors,
        )

    # =====================================================
    # Invalid Authentication Type
    # =====================================================

    def test_invalid_authentication_type(self):

        data = get_valid_architecture()

        data["security"]["authentication_type"] = "InvalidAuth"

        serializer = ArchitectureSerializer(
            data=data
        )

        self.assertFalse(
            serializer.is_valid()
        )

        self.assertIn(
            "security",
            serializer.errors,
        )