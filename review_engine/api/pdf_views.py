from tempfile import NamedTemporaryFile

from django.http import FileResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from review_engine.repository.review_repository import (
    ReviewRepository,
)

from review_engine.reports.pdf_generator import (
    PDFGenerator,
)
from review_engine.logging.logger import (
    logger,
)
logger = logger.get_logger()


class ReviewPDFAPIView(APIView):
    permission_classes=[IsAuthenticated]
    """
    GET /api/history/reviews/<review_id>/pdf/
    """

    def get(
        self,
        request,
        review_id,
    ):

        logger.info(f"Generating PDF for review {review_id}")
        repository = ReviewRepository()

        review = repository.get_review(
            request.user,
            review_id,
        )

        if review is None:

            return Response(
                {
                    "message": "Review not found."
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        with NamedTemporaryFile(
            suffix=".pdf",
            delete=False,
        ) as temp_file:
            

            PDFGenerator().generate(
                review=review,
                output_path=temp_file.name,
            )
            logger.info("PDF generated successfully. ")

            return FileResponse(
                open(temp_file.name, "rb"),
                as_attachment=True,
                filename=f"{review['system_name']}_review.pdf",
                content_type="application/pdf",
            )