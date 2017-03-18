from django.conf.urls import url

from .views import (
    blog_home,
    article_detail,
    article_create,
    article_update,
    article_delete
)


urlpatterns = [
    url(r'^$', blog_home, name='blog-home'),
    url(r'^(?P<pk>\d+)/$', article_detail, name='article-detail'),
    url(r'^create/$', article_create, name='article-create'),
    url(r'^(?P<pk>\d+)/update$', article_update, name='article-update'),
    url(r'^(?P<pk>\d+)/delete$', article_delete, name='article-delete'),
]
