from django.conf.urls import url
from snippets.api.views import snippet_list, snippet_detail

urlpatterns = [
    url(r'^$', snippet_list),
    url(r'^(?P<pk>[0-9]+)$', snippet_detail)
]
