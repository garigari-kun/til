from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Post
from .forms import PostModelForm
from .decorators import is_post_author


# @login_required
def index(request):
    template_name = 'index.html'
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, template_name, context)


@login_required
def create_post(request):
    template_name = 'create_post.html'
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
    else:
        form = PostModelForm()
    context = {
        'form': form,
    }
    return render(request, template_name, context)



@login_required
@is_post_author
def edit_post(request, pk):
    template_name = 'edit_post.html'
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')
    else:
        form = PostModelForm(instance=post)
    context = {
        'form': form,
    }
    return render(request, template_name, context)
