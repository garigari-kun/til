from django.conf.urls import url

from .views import (
    IndexView,
    SignUpView,
    validate_username
)

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^signup$', SignUpView.as_view(), name='signup'),
    url(r'^ajax/validate_username/$', validate_username, name='validate_username'),

]
