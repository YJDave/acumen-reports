import os
from httplib2 import Http

from django.contrib.auth import views
from django.core.urlresolvers import reverse_lazy
from . import forms
from django.contrib.auth.decorators import login_required
from googleapiclient.discovery import build
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render
from oauth2client.contrib import xsrfutil
from oauth2client.client import flow_from_clientsecrets
from oauth2client.contrib.django_util.storage import DjangoORMStorage
from django.conf import settings
from .models import AnalyticsAuth
# Create your views here.


class AccountSetupView(views.FormView):
    template_name = 'analytics/account_setup.html'
    form_class = forms.AccountSetupForm
    success_url = reverse_lazy('analytics: prop_settings')
    pass


class PropertySettingsView(views.FormView):
    template_name = 'analytics/prop_settings.html'
    form_class = forms.PropertyForm
    success_url = reverse_lazy('analytics: dashboard')
    pass


REDIRECT_URI = 'http://localhost:8000/analytics/oauth2callback'
CLIENT_SECRETS = os.path.join(os.path.dirname(__file__), 'client_secrets.json')
FLOW = flow_from_clientsecrets(
    CLIENT_SECRETS,
    scope='https://www.googleapis.com/auth/analytics.readonly',
    redirect_uri=REDIRECT_URI)


def get_accounts_ids(service):
    accounts = service.management().accounts().list().execute()
    ids = []
    if accounts.get('items'):
        for account in accounts['items']:
            ids.append(account['id'])
    return ids


@login_required
def authorize(request):
    storage = DjangoORMStorage(
        AnalyticsAuth, 'id', request.user, 'credential')
    credential = storage.get()
    if credential is None or credential.invalid:
        FLOW.params['state'] = xsrfutil.generate_token(settings.SECRET_KEY,
                                                       request.user)
        authorize_url = FLOW.step1_get_authorize_url()
        return HttpResponseRedirect(authorize_url)
    else:
        service = build("analytics", "v3", http=credential.authorize(Http()))
        ids = get_accounts_ids(service)
        return render(
            request, 'analytics/success.html', {'ids': ids})


@login_required
def auth_return(request):
    print(request.GET['state'][0].encode('utf-8'))
    print(settings.SECRET_KEY, request.user)
    if not xsrfutil.validate_token(settings.SECRET_KEY,
                                   request.GET['state'].encode('utf-8'),
                                   request.user):
        print("here")
        return HttpResponseBadRequest()
    credential = FLOW.step2_exchange(request.GET)
    storage = DjangoORMStorage(
        AnalyticsAuth, 'id', request.user, 'credential')
    storage.put(credential)
    return HttpResponseRedirect("/analytics")
