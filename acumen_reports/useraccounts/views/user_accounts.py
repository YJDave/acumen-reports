import acumen_reports.generics as generic_views

from django.contrib.auth import views as auth_views
from . import forms
from allauth.account import views as allauth_views
from django.contrib import messages
from .models import User
from django.core.urlresolvers import reverse_lazy


class RegisterView(allauth_views.SignupView):
    form_class = forms.RegisterForm


class UserDashboard(generic_views.TemplateView):
    template_name = "useraccounts/user-dashboard.html"
    pass


class UserSettings(generic_views.UpdateView):
    model = User
    template_name = "useraccounts/user-settings.html"
    form_class = forms.UserSettingsForm

    def get_success_url(self):
        return reverse_lazy('user_settings', kwargs={
            'user_name': self.object.username})

    def get_form_kwargs(self, *args, **kwargs):
        form_kwargs = super().get_form_kwargs(*args, **kwargs)
        form_kwargs['request'] = self.request
        return form_kwargs

    def get_object(self, *args, **kwargs):
        return self.request.user

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS,
                             ("Successfully updated profile information"))

        return super().form_valid(form)

    def form_invalid(self, form):
        messages.add_message(
            self.request,
            messages.ERROR,
            ("Failed to update profile information."))
        return super().form_invalid(form)
