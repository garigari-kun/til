from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .forms import PostModelForm
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
    template_name = 'post_form.html'
    form = PostModelForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

    context = {
        'form': form
    }
    return render(request, template_name, context)
    # return HttpResponse('Create')

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
