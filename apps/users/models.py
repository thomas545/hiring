from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseUser(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True, null=True)
