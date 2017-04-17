from django.conf.urls import url

from .views import post_list, post_create, post_update, post_delete, post_detail

urlpatterns = [
    url(r'^$', post_list),
    url(r'^create/$', post_create),
    url(r'^update/$', post_update),
    url(r'^delete/$', post_delete),
    url(r'^(?P<id>\d+)/$', post_detail),

]
