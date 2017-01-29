from django.conf.urls import url
from snippets.api.views import SnippetList, SnippetDetail, SnippetHighlight, SnippetViewSet
from rest_framework import renderers

snippet_list = SnippetViewSet.as_view(
    {
        'get': 'list',
        'post': 'create'
    }
)

snippet_detail = SnippetViewSet.as_view(
    {
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }
)

snippet_highlight = SnippetViewSet.as_view(
    {
        'get': 'highlight',

    },
    renderer_classes = [renderers.StaticHTMLRenderer]
)


urlpatterns = [
    url(r'^$', snippet_list, name='snippet-list'),
    url(r'^(?P<pk>[0-9]+)$', snippet_detail, name='snippet-detail'),
    url(r'^(?P<pk>[0-9]+)/highlight', snippet_highlight, name='snippet-highlight'),
]



    # url(r'^snippets/(?P<pk>[0-9]+)/highlight', SnippetHighlight.as_view()),
