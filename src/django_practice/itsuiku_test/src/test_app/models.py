from django.conf import settings
from django.db import models





class Schedule(models.Model):
    date = models.DateField()
    time = models.TimeField()
    is_allday = models.BooleanField(default=False)

    def __str__(self):
        return '{}: {}'.format(self.date, self.time)


class Event(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=120)
    description = models.TextField()
    schedule = models.ManyToManyField(Schedule)

    def __str__(self):
        return str(self.title)


class Attendance(models.Model):
    AT_CHOICES = (
        ('yes', 'yes'),
        ('mmm', 'mmm'),
        ('no', 'no')
    )
    event = models.ForeignKey(Event)
    schedule = models.ForeignKey(Schedule)
    choice = models.CharField(choices=AT_CHOICES, max_length=3)

    def __str__(self):
        return '{}: {}'.format(self.schedule.date, self.schedule.time)

class Invitee(models.Model):
    name = models.CharField(max_length=120)
    comment = models.CharField(max_length=120)
    event = models.ForeignKey(Event)
    attendances = models.ManyToManyField(Attendance)

    def __str__(self):
        return str(self.name)
