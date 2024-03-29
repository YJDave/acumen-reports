from django.conf.urls import url, include

from .views.projects import (
    CreateProject,
    ListAllProjects,
    ProjectDashboard,
    ProjectHistory,
    ProjectReports,
    ProjectSettings,
)

from .views.profiles import (
    CreateProfile,
    ProfileDashboard,
    ProfileReports,
    ListAllProfiles,
)


profile_urls = [
    url(r'^$', ProfileDashboard.as_view(),
        name='profile_dashboard'),
    url(r'^reports/$', ProfileReports.as_view(), name='profile_reports'),
]

main_profile_urls = [
    url(r'^$', ListAllProfiles.as_view(), name='all_profiles'),
    url(r'^create/$', CreateProfile.as_view(), name='create_profile'),
    url(r'^create/', include('integrations.urls')),
    url(r'^(?P<profile_id>\d+)/', include(profile_urls)),
]

# TODO: History of project, profile, report will list
# all past events or user actions of particular project,
# profile or report. For this, we have to create one model
# which stores logs of user actions and automatic events.

# TODO: Rather than having reports and report history in every
# tab, i.e. project, profile we can just add filters on all
# reports tab to filter report by project, profile etc.

project_urls = [
    url(r'^$', ProjectDashboard.as_view(), name='project_dashboard'),

    url(r'^settings/$', ProjectSettings.as_view(), name='project_settings'),
    url(r'^reports/$', ProjectReports.as_view(), name='project_reports'),
    url(r'^history/$', ProjectHistory.as_view(), name='project_history'),

    url(r'^profiles/', include(main_profile_urls)),
]

urlpatterns = [
    url(r'^$',
        ListAllProjects.as_view(), name='all_projects'),
    url(r'^create/$',
        CreateProject.as_view(), name='create_project'),
    url(r'^(?P<proj_id>\d+)/', include(project_urls)),
]
