from django.contrib.auth import views

class HomePage(views.TemplateView):
    template_name = 'index.html'
    pass

class UserDashboard(views.TemplateView):
    template_name = "useraccounts/user-dashboard.html"
    pass

class UserSettings(views.TemplateView):
    template_name = "useraccounts/user-settings.html"
    pass
