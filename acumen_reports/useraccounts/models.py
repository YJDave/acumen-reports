from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    full_name = models.CharField(max_length=250, blank=True)
