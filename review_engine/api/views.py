from django.conf import settings

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from review_engine.api.serializers import ArchitectureSerializer
from review_engine.validators.architecture_validator import ArchitectureValidator
from review_engine.rules.rule_engine import RuleEngine
from review_engine.services.score_engine import ScoreEngine
from review_engine.services.response_builder import ResponseBuilder
from review_engine.services.llm_service import LLMService
from review_engine.rules.evaluator import (
    PASS,
    FAIL,
    NOT_EVALUATED)

from review_engine.repository.review_repository import ReviewRepository
from review_engine.logging.logger import logger
logger = logger.get_logger()

class ArchitectureReviewAPIView(APIView):

    permission_classes=[IsAuthenticated]

    def post(self, request):
        logger.info("Architecture review request received.")

        # -----------------------------------------
        # Serializer Validation
        # -----------------------------------------

        serializer = ArchitectureSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        validated_data = serializer.validated_data

        logger.info("Serializer validation successful.")

        # -----------------------------------------
        # Business Validation
        # -----------------------------------------

        ArchitectureValidator(
            validated_data
        ).validate()

        logger.info("Business validation successful.")
        # -----------------------------------------
        # Rule Engine
        # -----------------------------------------

        rule_result = RuleEngine(
            validated_data
        ).evaluate()

        passed=sum(
            1
            for rule in rule_result.rule_results
            if rule["status"] == PASS
        )
        failed=sum(
            1
            for rule in rule_result.rule_results
            if rule["status"] == FAIL
        )
        not_evaluated=sum(
            1
            for rule in rule_result.rule_results
            if rule["status"] == NOT_EVALUATED
        )
        

        logger.info(
            f"Rule evaluation completed."
            f"Passed: {passed},"
            f"failed: {failed},"
            f"Not evaluated: {not_evaluated},"
        )

        # -----------------------------------------
        # Score Engine
        # -----------------------------------------

        scores = ScoreEngine(
            rule_result
        ).calculate()

        logger.info(f"overall score calculated: {scores['overall_score']}")

        # -----------------------------------------
        # Build Response
        # -----------------------------------------

        response = ResponseBuilder(
            system_name=validated_data["system_name"],
            scores=scores,
            rule_result=rule_result,
        ).build()

        # -----------------------------------------
        # LLM Analysis
        # -----------------------------------------
        logger.info("Starting LLM analysis.")

        
        if settings.ENABLE_LLM:
            llm_analysis = LLMService(
                api_key=settings.GEMINI_API_KEY,
                ).analyze(
                architecture=validated_data,
                scores=scores,
                strengths=response["strengths"],
                weaknesses=response["weaknesses"],
                recommendations=response["recommendations"],
    )
        else:
            llm_analysis = "AI analysis is disabled."
        
        response["llm_analysis"] = llm_analysis
        logger.info("LLM analysis completed.")

        # -----------------------------------------
        # Save Review
        # -----------------------------------------

        repository = ReviewRepository()

        saved_review = repository.save_review(
                    user=request.user,
                    architecture=validated_data,
                     review_result=response,
                    )

        response["review_id"] = saved_review["review_id"]
        logger.info(f"review saved successfully with review_id: {saved_review['review_id']}")
        # -----------------------------------------
        # Return Response
        # -----------------------------------------
        logger.info("Architecture review process completed successfully.")
        return Response(
            response,
            status=status.HTTP_200_OK,
        )