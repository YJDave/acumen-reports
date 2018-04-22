from django.contrib.auth import views

class ProjectDashboard(views.TemplateView):
    template_name = "projects/dashboard.html"
    pass

class ProjectSettings(views.TemplateView):
    template_name = "projects/settings.html"
    pass

class ProjectReports(views.TemplateView):
    template_name = "projects/all-reports.html"
    pass

class ProjectHistory(views.TemplateView):
    template_name = "projects/history.html"
    pass

class CreateProject(views.TemplateView):
    template_name = "projects/create.html"
    pass

class ListAllProjects(views.TemplateView):
    template_name = "projects/all-projects.html"
    pass
