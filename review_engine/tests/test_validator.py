from django.test import TestCase

from review_engine.validators.architecture_validator import (
    ArchitectureValidator,
)

from review_engine.exceptions.custom_exceptions import (
    ArchitectureValidationError,
)

from review_engine.tests.test_data import (
    get_valid_architecture,
)


class ArchitectureValidatorTests(TestCase):

    def test_valid_architecture(self):

        data = get_valid_architecture()

        validator = ArchitectureValidator(data)

        self.assertEqual(
            validator.validate(),
            []
        )

    def test_duplicate_service_names(self):

        data = get_valid_architecture()

        data["services"].append(
            data["services"][0].copy()
        )

        with self.assertRaises(
            ArchitectureValidationError
        ):
            ArchitectureValidator(data).validate()

    def test_empty_database_list(self):

        data = get_valid_architecture()

        data["databases"] = []

        with self.assertRaises(
            ArchitectureValidationError
        ):
            ArchitectureValidator(data).validate()

    def test_cache_without_type(self):

        data = get_valid_architecture()

        data["cache"]["enabled"] = True
        data["cache"]["type"] = None

        with self.assertRaises(
            ArchitectureValidationError
        ):
            ArchitectureValidator(data).validate()

    def test_message_queue_without_type(self):

        data = get_valid_architecture()

        data["message_queue"]["enabled"] = True
        data["message_queue"]["type"] = None

        with self.assertRaises(
            ArchitectureValidationError
        ):
            ArchitectureValidator(data).validate()

    def test_restore_without_backup(self):

        data = get_valid_architecture()

        data["backup"]["enabled"] = False
        data["backup"]["restore_tested"] = True

        with self.assertRaises(
            ArchitectureValidationError
        ):
            ArchitectureValidator(data).validate()

    def test_interface_without_layered_design(self):

        data = get_valid_architecture()

        data["architecture"]["layered_design"] = False
        data["architecture"]["interface_definition"] = True

        with self.assertRaises(
            ArchitectureValidationError
        ):
            ArchitectureValidator(data).validate()