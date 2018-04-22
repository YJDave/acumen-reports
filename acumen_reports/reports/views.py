from django.contrib.auth import views

class ListAllReports(views.TemplateView):
    template_name = "reports/all-reports.html"
    pass

class ReportDashboard(views.TemplateView):
    template_name = "reports/dashboard.html"
    pass

class ReportsHistory(views.TemplateView):
    template_name = "reports/all-history.html"
    pass

class CreateReport(views.TemplateView):
    template_name = "reports/create.html"
    pass

class ReportSetting(views.TemplateView):
    template_name = "reports/settings.html"
    pass
