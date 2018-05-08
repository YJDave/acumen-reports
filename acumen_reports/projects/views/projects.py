from django.contrib.auth import views
from django.contrib.auth.mixins import LoginRequiredMixin

# Project views


class ProjectDashboard(LoginRequiredMixin, views.TemplateView):
    template_name = "projects/dashboard.html"
    pass


class ProjectSettings(LoginRequiredMixin, views.TemplateView):
    template_name = "projects/settings.html"
    pass


class ProjectReports(LoginRequiredMixin, views.TemplateView):
    template_name = "projects/all-reports.html"
    pass


class ProjectHistory(LoginRequiredMixin, views.TemplateView):
    template_name = "projects/history.html"
    pass


class CreateProject(LoginRequiredMixin, views.TemplateView):
    template_name = "projects/create.html"
    pass


class ListAllProjects(LoginRequiredMixin, views.TemplateView):
    template_name = "projects/all-projects.html"
    pass
