from django.conf.urls import url, include

from .views import (
	ReportDashboard,
	ReportSetting,
	ListAllReports,
	ReportsHistory,
	CreateReport,
)

report_urls = [
    url(r'^$', ReportDashboard.as_view(), name='report_dashboard'),
    url(r'^settings', ReportSetting.as_view(), name='report_setting'),
]

urlpatterns =[

    url(r'^$',
        ListAllReports.as_view(), name='all_reports'),
    url(r'^history/$',
        ReportsHistory.as_view(), name='all_reports_history'),
    url(r'^create/$',
        CreateReport.as_view(), name='create_report'),
    url(r'^(?P<report_id>\d+)/', include(report_urls)),
]
