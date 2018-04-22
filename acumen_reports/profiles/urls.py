from django.conf.urls import url, include

from .views import (
	CreateProfile,
	ProjectProfileDashboard,
	ProfileReports,
)

profile_urls = [
    url(r'^$', ProjectProfileDashboard.as_view(),
        name='project_profile_dashboard'),
    url(r'^reports/$', ProfileReports.as_view(), name='profile_reports'),
]

urlpatterns = [
    url(r'^create/$', CreateProfile.as_view(), name='create_profile'),
    url(r'^create/analytics/', include('analytics.urls')),
    url(r'^(?P<profile_id>\d+)/', include(profile_urls)),
]
