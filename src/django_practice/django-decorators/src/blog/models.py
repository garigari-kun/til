from django.db import models

from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.title)
