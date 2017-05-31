from django.conf import settings
from django.db import models



class Schedule(models.Model):
    date = models.DateField(null=True, blank=True)
    comment = models.CharField(max_length=120, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return '{}: {} {}'.format(self.pk, self.date, self.comment)


class Event(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    schedule_range = models.ManyToManyField(Schedule, blank=True, verbose_name='schedule_range')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return '{}: {}'.format(self.pk, self.title)
