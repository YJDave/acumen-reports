from django.conf.urls import url, include
from django.contrib import admin
from useraccounts.views.home import HomePage
from useraccounts.views.user_accounts import RegisterView
from allauth.account import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomePage.as_view(), name="home"),
    url(r'^accounts/signup/$', RegisterView.as_view(), name='account_signup'),
    url(r'^accounts/login/$', views.LoginView.as_view(), name='account_login'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^(?P<user_name>\w+)/', include('useraccounts.urls')),
    url(r'^integrations/', include('integrations.urls')),
]
