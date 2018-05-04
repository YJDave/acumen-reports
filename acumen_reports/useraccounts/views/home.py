from django.contrib.auth import views

class HomePage(views.TemplateView):
    template_name = 'index.html'
    pass
