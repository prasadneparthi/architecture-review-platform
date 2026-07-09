from django.urls import path

from review_engine.api.pdf_views import (
    ReviewPDFAPIView,
)

urlpatterns = [

    path(
        "reviews/<str:review_id>/pdf/",
        ReviewPDFAPIView.as_view(),
        name="review-pdf",
    ),

]