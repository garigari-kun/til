from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect

from .forms import ArticleModelForm
from .models import Article



def blog_home(request):
    template_name = 'articles/articles_home.html'
    article_list = Article.objects.all()
    context = {
        'article_list': article_list
    }
    return render(request, template_name, context)


def article_detail(request, pk):
    template_name = 'articles/article.html'
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, template_name, context)


def article_create(request):
    template_name = 'articles/article_create.html'
    if request.method == 'POST':
        form = ArticleModelForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.get(username=request.user.username)
            instance = form.save(commit=False)
            instance.author = user
            instance.save()
            return HttpResponseRedirect(form.instance.get_absolute_url())
    else:
        form = ArticleModelForm()

    context = {
    'form': form
    }

    return render(request, template_name, context)



def article_update(request, pk):
    template_name = 'articles/article_update.html'
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        form = ArticleModelForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            user = User.objects.get(username=request.user.username)
            instance = form.save(commit=False)
            instance.author = user
            instance.save()
            return HttpResponseRedirect(instance.get_absolute_url())
    else:
        form = ArticleModelForm(instance=article)

    context = {
    'form': form
    }

    return render(request, template_name, context)



def article_delete(request, pk):
    success_url = reverse_lazy('blog-home')
    article = Article.objects.get(pk=pk)
    if request.method == 'POST' and 'delete' in request.POST:
        article.delete()
        return HttpResponseRedirect(success_url)
    else:
        return HttpResponseRedirect(article.get_absolute_url())
