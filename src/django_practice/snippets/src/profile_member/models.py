from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)


class FamilyMember(models.Model):
    profile = models.ForeignKey(Profile)
    name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=100)


    
