from django.contrib.auth import views
from django.contrib.auth.mixins import LoginRequiredMixin


class AnalyticsSetup(LoginRequiredMixin, views.TemplateView):
    template_name = 'analytics/setup.html'
    pass
