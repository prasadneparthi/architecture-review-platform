from django.urls import path
from frontend.views import (
    DashboardView,
    HomeView,
    LoginView,
    RegisterView,
    NewReviewView,
    ReviewResultView,
    HistoryView,
)
from django.views.generic import TemplateView
urlpatterns=[
    path("",HomeView.as_view(),name="home"),
    path("login/",LoginView.as_view(),name="frontend-login"),
    path("register/",RegisterView.as_view(),name="frontend-register"),
    path("dashboard/",DashboardView.as_view(),name="dashboard"),
    path("review/new/",NewReviewView.as_view(),name="new-review"),
    path("review/result/",ReviewResultView.as_view(),name="review-result,"),
    path("history/",HistoryView.as_view(),name="history"),
    path("account/",TemplateView.as_view(template_name="dashboard/account.html"),name="account"),
]