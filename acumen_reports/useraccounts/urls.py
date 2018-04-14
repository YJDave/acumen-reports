from django.conf.urls import url, include
from .views import (
	HomePage,
	UserDashboard,
	ProjectDashboard,
	ProjectProfileDashboard,
	ProjectSettings,
	ProfileSettings,
	ProjectReports,
	AddProfile,
	ListAllProjects,
	ListAllReports,
	UserSettings,
	ReportDashboard,
)

from analytics.views import (
	AnalyticsSetup,
)

analytics_urls = [
	url(r'^setup/$', AnalyticsSetup.as_view(), name='analytics_setup'),
]

profile_urls = [
    url(r'^$', ProjectProfileDashboard.as_view(), name='project_profile_dashboard'),
    url(r'^settings/$', ProfileSettings.as_view(), name='profile_settings'),
]

project_urls = [
	url(r'^$', ProjectDashboard.as_view(), name='project_dashboard'),

    url(r'^add/$', AddProfile.as_view(), name='add_profile'),
    url(r'^add/analytics/', include(analytics_urls)),

    url(r'^settings/$', ProjectSettings.as_view(), name='project_settings'),
    url(r'^reports/$', ProjectReports.as_view(), name='project_reports'),
    url(r'^reports/(?P<report_id>\d+)/', ReportDashboard.as_view(), name='report_dashboard'),

    url(r'^(?P<profile_id>\d+)/', include(profile_urls)),
]

urlpatterns = [
    url(r'^$', HomePage.as_view(), name='home'),
    url(r'^(?P<user_name>\w+)/$', UserDashboard.as_view(), name='user_dashboard'),
    url(r'^(?P<user_name>\w+)/projects/$', ListAllProjects.as_view(), name='all_projects'),
    url(r'^(?P<user_name>\w+)/reports/$', ListAllReports.as_view(), name='all_reports'),
    url(r'^(?P<user_name>\w+)/settings/$', UserSettings.as_view(), name='user_settings'),
    url(r'^(?P<user_name>\w+)/(?P<proj_id>\d+)/', include(project_urls)),
]
