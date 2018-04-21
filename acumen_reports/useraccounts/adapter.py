from django.conf import settings
from django.shortcuts import resolve_url
from allauth.account import adapter


class DefaultAccountAdapter(adapter.DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        """
        Returns the default URL to redirect to after logging in.  Note
        that URLs passed explicitly (e.g. by passing along a `next`
        GET parameter) take precedence over the value returned here.
        """
        assert request.user.is_authenticated
        url = settings.LOGIN_REDIRECT_URL + request.user.username + '/'

        return resolve_url(url)
