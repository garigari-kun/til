
from django.conf.urls import include, url

from .views import ReportView


urlpatterns = [
    url(r'^$', ReportView.as_view(), name="report"),
]
