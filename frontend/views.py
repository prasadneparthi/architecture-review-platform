from django.views.generic import TemplateView


class HomeView(TemplateView):

    template_name = "home.html"


class LoginView(TemplateView):

    template_name = "auth/login.html"


class RegisterView(TemplateView):

    template_name = "auth/register.html"


class DashboardView(TemplateView):

    template_name = "dashboard/dashboard.html"

class NewReviewView(TemplateView):
    template_name="dashboard/new_review.html"

class ReviewResultView(TemplateView):
    template_name="dashboard/review_result.html"

class HistoryView(TemplateView):
    template_name="dashboard/history.html"