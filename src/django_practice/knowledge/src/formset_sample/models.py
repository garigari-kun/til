from django.db import models

from django.utils import timezone

class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)

class FamilyMember(models.Model):
    profile = models.ForeignKey(Profile)
    name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=100)
