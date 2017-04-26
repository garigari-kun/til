from django.conf.urls import url

from .views import IndexView, SignUpView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^signup$', SignUpView.as_view(), name='signup'),

]
