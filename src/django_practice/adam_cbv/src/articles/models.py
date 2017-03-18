from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models



class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=40)
    headline = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)


    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk': self.id})
