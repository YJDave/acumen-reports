from django.conf.urls import url, include
from .views.analytics import (
	AnalyticsSetup,
)

analytics_urls = [
    url(r'^setup/$', AnalyticsSetup.as_view(), name='analytics_setup'),
]

urlpatterns = [
    url(r'^analytics/', include(analytics_urls)),
]
