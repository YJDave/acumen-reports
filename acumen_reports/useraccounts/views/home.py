from django.contrib.auth import views as auth_views


class HomePage(auth_views.TemplateView):
    template_name = 'index.html'
    pass
