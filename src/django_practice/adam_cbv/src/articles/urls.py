from django.conf.urls import url

from .views import (
    blog_home,
    article_detail,
    article_create,
    article_update,
    article_delete,
    BlogHomeListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView
)


urlpatterns = [
    url(r'^$', BlogHomeListView.as_view(), name='blog-home'),
    url(r'^(?P<pk>\d+)/$', ArticleDetailView.as_view(), name='article-detail'),
    url(r'^create/$', ArticleCreateView.as_view(), name='article-create'),
    url(r'^(?P<pk>\d+)/update$', ArticleUpdateView.as_view(), name='article-update'),
    url(r'^(?P<pk>\d+)/delete$', ArticleDeleteView.as_view(), name='article-delete'),
]
