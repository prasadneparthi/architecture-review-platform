from django.urls import path

from review_engine.api.history_views import (
    ReviewListAPIView,
    ReviewDetailAPIView,
)

urlpatterns = [

    path(
        "reviews/",
        ReviewListAPIView.as_view(),
        name="review-list",
    ),

    path(
        "reviews/<str:review_id>/",
        ReviewDetailAPIView.as_view(),
        name="review-detail",
    ),

    

]