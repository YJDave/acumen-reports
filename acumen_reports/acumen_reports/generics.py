import django.views.generic as base
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class UpdateView(base.UpdateView):
    pass


@method_decorator(login_required, name='dispatch')
class FormView(base.FormView):
    pass


@method_decorator(login_required, name='dispatch')
class TemplateView(base.TemplateView):
    pass


@method_decorator(login_required, name='dispatch')
class CreateView(base.CreateView):
    pass


@method_decorator(login_required, name='dispatch')
class ListView(base.ListView):
    pass
