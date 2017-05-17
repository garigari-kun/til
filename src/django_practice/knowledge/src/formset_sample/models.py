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




class Schedule(models.Model):
    date = models.DateField(null=True, blank=True)
    comment = models.CharField(max_length=120, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return '{}: {} {}'.format(self.pk, self.date, self.comment)
