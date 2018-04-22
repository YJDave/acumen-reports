from django.contrib.auth import views


class CreateProfile(views.TemplateView):
    template_name = "profiles/create.html"
    pass


class ProjectProfileDashboard(views.TemplateView):
    template_name = "profiles/dashboard.html"
    pass


class ProfileReports(views.TemplateView):
    template_name = "profiles/all-reports.html"
    pass


class ListAllProjectProfiles(views.TemplateView):
    template_name = "profiles/all-project-profiles.html"
    pass
