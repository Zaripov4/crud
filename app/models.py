from django.db import models
from datetime import timezone
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    dob = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'users'
