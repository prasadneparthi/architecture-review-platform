from django.urls import path
from .views import ArchitectureReviewAPIView
from review_engine.api.account_views import ProfileAPIView,ChangePasswordAPIView, DeleteAccountAPIView

urlpatterns = [
    path('review/', ArchitectureReviewAPIView.as_view(), name='architecture-review'),
    path('auth/profile/', ProfileAPIView.as_view(), name='profile'),
    path('auth/change-password/', ChangePasswordAPIView.as_view(), name='change-password'),
    path('auth/delete-account/', DeleteAccountAPIView.as_view(), name='delete-account'),
]