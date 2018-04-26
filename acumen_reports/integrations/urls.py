from django.conf.urls import url, include
from .views.analytics import (
    AuthorizeAnalytics,
    AuthReturn,
)

analytics_urls = [
    url(r'^setup/$', AuthorizeAnalytics.as_view(), name='analytics_setup'),
    url(r'^oauth2callback/', AuthReturn.as_view(), name='auth_return'),
]

urlpatterns = [
    url(r'^analytics/', include(analytics_urls)),
]
