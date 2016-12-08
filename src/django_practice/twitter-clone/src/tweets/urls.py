from django.conf.urls import url

# from .views import tweet_list_view, tweet_detail_view
from .views import TweetListView, TweetDetailView, TweetCreateView

urlpatterns = [
    # url(r'^$', tweet_list_view, name='list'),
    # url(r'^(?P<pk>\d+)$', tweet_detail_view, name='detail'),
    url(r'^$', TweetListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', TweetDetailView.as_view(), name='detail'),
    url(r'^create/$', TweetCreateView.as_view(), name='create'),
]
