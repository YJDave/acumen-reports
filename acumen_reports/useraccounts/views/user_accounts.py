from django.contrib.auth import views
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from . import forms
from allauth.account import views as allauth_views


class RegisterView(allauth_views.SignupView):
    form_class = forms.RegisterForm


@method_decorator(login_required, name='dispatch')
class UserDashboard(views.TemplateView):
    template_name = "useraccounts/user-dashboard.html"
    pass


class UserSettings(views.TemplateView):
    template_name = "useraccounts/user-settings.html"
    pass
