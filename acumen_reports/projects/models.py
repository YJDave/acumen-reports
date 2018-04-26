from django.db import models
from integrations.models import (
    ProfileAuth,
)
from useraccounts.models import User


class Project(models.Model):
    # FEATURE: Allow user to add tags in projects and
    # filter projects using tags as well.
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1500)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    # TODO: Remove hard coded integration types
    INTEGRATION_CHOICES = (
        ("00", "Google analytics"),
        ("01", "Google search console"),
    )

    # This will include all profiles which are added by user
    # using different integration.
    # Though, how to map this to integration type's authentication
    # model is not clear yet.
    # TODO: Relate this model with integration-authentication model.
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    created_date = models.DateTimeField(auto_now_add=True)
    auth = models.ForeignKey(ProfileAuth, on_delete=models.CASCADE)
    integration_type = models.CharField(
        max_length=2, choices=INTEGRATION_CHOICES, default='00')
