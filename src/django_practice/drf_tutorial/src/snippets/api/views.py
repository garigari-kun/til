from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView, GenericAPIView
from rest_framework import permissions
from snippets.models import Snippet
from snippets.api.serializers import SnippetSerializer, UserSerializer
from snippets.api.permissions import IsOwnerOrReadOnly

from rest_framework.decorators import api_view
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework import viewsets
from rest_framework.decorators import detail_route

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
        }
    )


class SnippetHighlight(GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        # print(snippet)
        return Response(snippet.highlighted)



class SnippetList(ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,

    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



# New viewsets version

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class SnippetViewSet(viewsets.ModelViewSet):

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)






















# end
