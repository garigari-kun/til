from django.db import models

class JobList(models.Model):
    jobtitle = models.CharField(max_length=100)
    jobdescription = models.CharField(max_length=300)
    postdate = models.DateField(auto_now_add=True)
