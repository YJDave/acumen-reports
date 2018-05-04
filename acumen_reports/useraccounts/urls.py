from django.conf.urls import url, include
from .views.user_accounts import (
    UserDashboard,
    UserSettings,
)

urlpatterns = [
    url(r'^$',
        UserDashboard.as_view(), name='user_dashboard'),
    url(r'^settings/$',
        UserSettings.as_view(), name='user_settings'),
    url(r'^projects/', include('projects.urls')),
    url(r'^reports/', include('reports.urls')),
]
