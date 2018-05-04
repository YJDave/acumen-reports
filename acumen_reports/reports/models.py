from django.db import models
from multi_email_field.fields import MultiEmailField
from projects.models import (
	Project,
)

class Report(models.Model):
    # TODO: Remove hard coded report types
    # Currently report types are hard coded. According to these types
    # which template should be used to generate report can be decide.
    REPORT_TYPE = (
        ("00", "Report type 1"),
        ("01", "Report type 2"),
    )

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    created_date = models.DateTimeField(auto_now_add=True)

    # FEATURE: Allow user to create user groups, i.e. default user groups,
    # admin user group etc.
    # FEATURE: Allow user to directly add user groups(group of emails)
    emails_to_send = MultiEmailField()
