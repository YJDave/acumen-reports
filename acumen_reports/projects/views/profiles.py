from django.contrib.auth import views
from django.contrib.auth.mixins import LoginRequiredMixin
# Profile views


class CreateProfile(LoginRequiredMixin, views.TemplateView):
    template_name = "profiles/create.html"
    pass


class ProfileDashboard(LoginRequiredMixin, views.TemplateView):
    template_name = "profiles/dashboard.html"
    pass


class ProfileReports(LoginRequiredMixin, views.TemplateView):
    template_name = "profiles/all-reports.html"
    pass


class ListAllProfiles(LoginRequiredMixin, views.TemplateView):
    template_name = "profiles/all-profiles.html"
    pass
