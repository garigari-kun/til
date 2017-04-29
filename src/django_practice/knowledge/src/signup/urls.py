
from django.conf.urls import include, url

from .views import SignupView

urlpatterns = [
    url(r'^$', SignupView.as_view(), name='signup'),

]
