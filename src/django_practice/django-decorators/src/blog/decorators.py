from django.core.exceptions import PermissionDenied
from .models import Post

def is_post_author(function):
    def wrap(request, *args, **kwargs):
        post = Post.objects.get(pk=kwargs['pk'])
        if post.author == request.user:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap
