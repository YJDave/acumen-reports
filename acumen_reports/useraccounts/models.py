from django.db import models
from django.contrib.auth.models import User
from multi_email_field.fields import MultiEmailField


class UserProject(models.Model):
    # FEATURE: Allow user to add tags in projects and
    # filter projects using tags as well.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1500)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProjectProfile(models.Model):
    # TODO: Remove hard coded integration types
    INTEGRATION_CHOICES = (
        ("00", "Google analytics"),
        ("01", "Google search console"),
    )

    # This will include all profiles which are added by user
    # using different integration.
    # Though, how to map this to integration type's authentication model is not clear yet.
    # TODO: Relate this model with integration-authentication model.
    project = models.ForeignKey(UserProject, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    created_date = models.DateTimeField(auto_now_add=True)
    integration_type = models.CharField(
        max_length=2, choices=INTEGRATION_CHOICES, default='00')


class ProjectReport(models.Model):
    # TODO: Remove hard coded report types
    # Currently report types are hard coded. According to these types
    # which template should be used to generate report can be decide.
    REPORT_TYPE = (
        ("00", "Report type 1"),
        ("01", "Report type 2"),
    )

    project = models.ForeignKey(UserProject, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    created_date = models.DateTimeField(auto_now_add=True)

    # FEATURE: Allow user to create user groups, i.e. default user groups,
    # admin user group etc.
    # FEATURE: Allow user to directly add user groups(group of emails)
    emails_to_send = MultiEmailField()
