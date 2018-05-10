from httplib2 import Http
import django.views.generic as base

from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from googleapiclient.discovery import build
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render
from oauth2client.contrib import xsrfutil
from oauth2client.client import flow_from_clientsecrets
from oauth2client.contrib.django_util.storage import DjangoORMStorage
from django.conf import settings
from integrations.models import AnalyticsCredentialModel, FlowModel
# from django.contrib.sites.shortcuts import get_current_site
# Create your views here.


def get_accounts_ids(service):
    accounts = service.management().accounts().list().execute()
    ids = []
    if accounts.get('items'):
        for account in accounts['items']:
            ids.append(account['id'])
    return ids


class AuthorizeAnalytics(LoginRequiredMixin, base.View):
    def dispatch(self, request):
        # REDIRECT_URI = "https://%s%s" % (get_current_site(request).domain,\
        # reverse("oauth2:return"))
        REDIRECT_URI = \
            'http://localhost:8000/integrations/analytics/oauth2callback'
        CLIENT_SECRETS = settings.GOOGLE_OAUTH2_CLIENT_SECRETS_JSON
        FLOW = flow_from_clientsecrets(
            CLIENT_SECRETS,
            scope='https://www.googleapis.com/auth/analytics.readonly',
            redirect_uri=REDIRECT_URI)

        user = request.user
        storage = DjangoORMStorage(
            AnalyticsCredentialModel, 'id', user, 'credential')
        credential = storage.get()
        if credential is None or credential.invalid is True:
            FLOW.params['state'] = xsrfutil.generate_token(settings.SECRET_KEY,
                                                           user)
            authorize_url = FLOW.step1_get_authorize_url()
            f = FlowModel(id=user, flow=FLOW)
            f.save()
            return HttpResponseRedirect(authorize_url)
        else:
            http = Http()
            http = credential.authorize(http)
            service = build("analytics", "v3", http=http)
            ids = get_accounts_ids(service)
            return render(
                request, 'analytics/success.html', {'ids': ids})


class AuthReturn(LoginRequiredMixin, base.RedirectView):
    def dispatch(self, request):
        user = request.user
        if not xsrfutil.validate_token(settings.SECRET_KEY,
                                       request.GET['state'].encode('utf-8'),
                                       user):
            return HttpResponseBadRequest()
        FLOW = FlowModel.objects.get(id=request.user).flow
        credential = FLOW.step2_exchange(request.GET)
        storage = DjangoORMStorage(
            AnalyticsCredentialModel, 'id', user, 'credential')
        storage.put(credential)
        return HttpResponseRedirect(reverse_lazy("analytics_setup"))
