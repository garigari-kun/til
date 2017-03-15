from django.conf import settings
from django.db import models

class SubReddit(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return str(self.title)



class Post(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    subreddit = models.ForeignKey(SubReddit)
    create_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return str(self.title)



class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey(Post)
    create_date = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.body)
