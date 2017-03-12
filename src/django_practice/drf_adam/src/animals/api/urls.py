from django.conf.urls import include, url
from rest_framework import routers

from .views import KittenViewSet, PuppyListCreateView, PuppyDetailUpdateDestroyView


router = routers.SimpleRouter()
router.register(r'', KittenViewSet)


urlpatterns = [
    url(r'^$', PuppyListCreateView.as_view(), name='puppy-list'),
    url(r'(?P<pk>\d+)/$', PuppyDetailUpdateDestroyView.as_view(), name='puppy-detail'),
]
