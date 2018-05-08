import django.views.generic as base
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from allauth.account import views as allauth_views
from useraccounts.models import User
from useraccounts import forms


class RegisterView(allauth_views.SignupView):
    form_class = forms.RegisterForm


class UserDashboard(LoginRequiredMixin, base.TemplateView):
    template_name = "useraccounts/user-dashboard.html"
    pass


class UserSettings(LoginRequiredMixin, base.UpdateView):
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
