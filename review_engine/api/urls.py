from django.urls import path
from .views import ArchitectureReviewAPIView

urlpatterns = [
    path('review/', ArchitectureReviewAPIView.as_view(), name='architecture-review'),
]