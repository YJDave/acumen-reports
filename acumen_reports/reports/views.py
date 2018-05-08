from django.contrib.auth import views
from django.contrib.auth.mixins import LoginRequiredMixin


class ListAllReports(LoginRequiredMixin, views.TemplateView):
    template_name = "reports/all-reports.html"
    pass


class ReportDashboard(LoginRequiredMixin, views.TemplateView):
    template_name = "reports/dashboard.html"
    pass


class ReportsHistory(LoginRequiredMixin, views.TemplateView):
    template_name = "reports/all-history.html"
    pass


class CreateReport(LoginRequiredMixin, views.TemplateView):
    template_name = "reports/create.html"
    pass


class ReportSetting(LoginRequiredMixin, views.TemplateView):
    template_name = "reports/settings.html"
    pass
