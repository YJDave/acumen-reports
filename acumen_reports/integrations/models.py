from django.db import models

# Derive every integration authentication model from this model, ex:
# class AnalyticsAuth(ProfileAuth):
#     auth_token = models.CharField(max_length=150)
class ProfileAuth(models.Model):
    pass

