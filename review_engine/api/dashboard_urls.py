from django.urls import path

from review_engine.api.dashboard_views import DashboardAPIView

urlpatterns = [

    path(
        "",
        DashboardAPIView.as_view(),
        name="dashboard-api",
    ),

]