from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from review_engine.repository.review_repository import (
    ReviewRepository,
)
from review_engine.logging.logger import (
    logger,
)
logger = logger.get_logger()


class ReviewListAPIView(APIView):
    permission_classes=[IsAuthenticated]
    """
    GET /api/history/reviews/
    """

    def get(self, request):
        logger.info("Fetching all review history")
        repository = ReviewRepository()

        reviews = repository.get_all_reviews(request.user,)

        return Response(
            reviews,
            status=status.HTTP_200_OK,
        )


class ReviewDetailAPIView(APIView):
    permission_classes=[IsAuthenticated]
    """
    GET /api/history/reviews/<review_id>/

    DELETE /api/history/reviews/<review_id>/
    """

    def get(
        self,
        request,
        review_id,
    ):
        logger.info(f"Fetching review history for review_id: {review_id}")
        repository = ReviewRepository()

        review = repository.get_review(
            request.user,
            review_id
        )

        if review is None:

            return Response(
                {
                    "message": "Review not found."
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(
            review,
            status=status.HTTP_200_OK,
        )

    def delete(
        self,
        request,
        review_id,
    ):
        logger.info(f"Deleting review {review_id}")
        repository = ReviewRepository()

        deleted = repository.delete_review(
            request.user,
            review_id,
        )

        if not deleted:

            return Response(
                {
                    "message": "Review not found."
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(
            {
                "message": "Review deleted successfully."
            },
            status=status.HTTP_200_OK,
        )