from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)
    is_agent = models.BooleanField(default=False)  # if you add staff later
    is_client = models.BooleanField(default=True)

    def __str__(self):
        return self.username
