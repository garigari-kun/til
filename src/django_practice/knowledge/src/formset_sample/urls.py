from django.conf.urls import include, url

from .views import CreateLinkView, ScheduleInputView

urlpatterns = [
    url(r'^$', CreateLinkView.as_view(), name='create-link'),
    url(r'^schedule$', ScheduleInputView.as_view(), name='create-schedule'),


]
