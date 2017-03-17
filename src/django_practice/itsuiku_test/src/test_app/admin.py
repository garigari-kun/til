from django.contrib import admin

from .models import Schedule, Event, Attendance, Invitee



admin.site.register(Schedule)
admin.site.register(Event)
admin.site.register(Attendance)
admin.site.register(Invitee)
