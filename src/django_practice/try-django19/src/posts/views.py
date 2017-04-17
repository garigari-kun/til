from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Post


def post_list(request):
    template_name = 'index.html'
    queryset = Post.objects.all()
    context = {
        'title': 'List',
        'object_list': queryset
    }
    # return HttpResponse('List')
    return render(request, template_name, context)

def post_create(request):
    return HttpResponse('Create')

def post_update(request):
    return HttpResponse('Update')

def post_delete(request):
    return HttpResponse('Delete')

def post_detail(request, id=None):
    template_name = 'post_detail.html'
    instance = get_object_or_404(Post, id=id)
    # return HttpResponse('Detail')
    context = {
        'title': 'Detail',
        'instance': instance,
    }
    return render(request, template_name, context)
