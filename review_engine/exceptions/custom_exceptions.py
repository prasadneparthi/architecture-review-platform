"""
Custom Exceptions

Defines all project-specific exceptions.
"""

from rest_framework.exceptions import APIException
from rest_framework import status


class ArchitectureReviewException(APIException):
    """
    Base exception for the Architecture Review project.
    """

    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = "Architecture review error occurred."
    default_code = "architecture_review_error"


class ArchitectureValidationError(APIException):
    """
    Raised when business validation fails.
    """

    status_code = status.HTTP_400_BAD_REQUEST
    default_code = "architecture_validation_error"

    def __init__(self, errors):

        super().__init__(
            detail={
                "success": False,
                "message": "Business validation failed.",
                "errors": errors,
            }
        )


class RuleEngineError(APIException):
    """
    Raised when rule engine execution fails.
    """

    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = "Rule engine execution failed."
    default_code = "rule_engine_error"


class LLMAnalysisError(APIException):
    """
    Raised when LLM analysis fails.
    """

    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = "LLM analysis failed."
    default_code = "llm_analysis_error"


class DatabaseError(APIException):
    """
    Raised when database operation fails.
    """

    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = "Database operation failed."
    default_code = "database_error"


class PDFGenerationError(APIException):
    """
    Raised when PDF generation fails.
    """

    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = "PDF generation failed."
    default_code = "pdf_generation_error"