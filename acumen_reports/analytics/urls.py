from django.conf.urls import url
from .views import (
	AnalyticsSetup,
)

urlpatterns = [
    url(r'^setup/$', AnalyticsSetup.as_view(), name='analytics_setup'),
]

