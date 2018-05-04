from django.contrib.auth import views

# Profile views

class CreateProfile(views.TemplateView):
    template_name = "profiles/create.html"
    pass

class ProfileDashboard(views.TemplateView):
    template_name = "profiles/dashboard.html"
    pass


class ProfileReports(views.TemplateView):
    template_name = "profiles/all-reports.html"
    pass


class ListAllProfiles(views.TemplateView):
    template_name = "profiles/all-profiles.html"
    pass
