from django.contrib.auth import views


class HomePage(views.TemplateView):
    template_name = 'index.html'
    pass


class UserDashboard(views.TemplateView):
    template_name = "useraccounts/user-dashboard.html"
    pass


class ProjectDashboard(views.TemplateView):
    template_name = "useraccounts/project-dashboard.html"
    pass


class ProjectProfileDashboard(views.TemplateView):
    template_name = "useraccounts/profile-dashboard.html"
    pass


class ProjectSettings(views.TemplateView):
    template_name = "useraccounts/project-settings.html"
    pass


class CreateProject(views.TemplateView):
    template_name = "useraccounts/project-create.html"
    pass


class ProfileSettings(views.TemplateView):
    template_name = "useraccounts/profile-settings.html"
    pass


class ProjectReports(views.TemplateView):
    template_name = "useraccounts/project-reports.html"
    pass


class AddProfile(views.TemplateView):
    template_name = "useraccounts/add-profile.html"
    pass


class ListAllProjects(views.TemplateView):
    template_name = "useraccounts/list-all-projects.html"
    pass


class ListAllReports(views.TemplateView):
    template_name = "useraccounts/list-all-reports.html"
    pass


class UserSettings(views.TemplateView):
    template_name = "useraccounts/user-settings.html"
    pass


class ReportDashboard(views.TemplateView):
    template_name = "useraccounts/report-dashboard.html"
    pass


class ReportsHistory(views.TemplateView):
    template_name = "useraccounts/report-history.html"
    pass


class CreateReport(views.TemplateView):
    template_name = "useraccounts/report-create.html"
    pass


class ProjectHistory(views.TemplateView):
    template_name = "useraccounts/project-history.html"
    pass


class ReportSetting(views.TemplateView):
    template_name = "useraccounts/report-setting.html"
    pass
