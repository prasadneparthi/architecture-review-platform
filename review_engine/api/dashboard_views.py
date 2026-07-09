from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from review_engine.repository.review_repository import ReviewRepository


class DashboardAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        repository = ReviewRepository()

        reviews = repository.get_all_reviews(request.user)

        total_reviews = len(reviews)

        if total_reviews == 0:

            average_score = 0
            latest_review = "-"

        else:

            average_score = round(
                sum(
                    r["review_result"]["overall_score"]
                    for r in reviews
                ) / total_reviews
            )

            latest_review = reviews[-1]["system_name"]

        return Response(
            {
                "total_reviews": total_reviews,
                "average_score": average_score,
                "latest_review": latest_review,
            }
        )