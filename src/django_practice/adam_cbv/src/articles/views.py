from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import ListView, RedirectView, DetailView, CreateView, UpdateView, DeleteView

from .forms import ArticleModelForm
from .models import Article



class BlogHomeListView(ListView):
    model = Article
    template_name = 'articles/articles_home.html'



def blog_home(request):
    template_name = 'articles/articles_home.html'
    article_list = Article.objects.all()
    context = {
        'article_list': article_list
    }
    return render(request, template_name, context)



class BlogHomeRedirectView(RedirectView):
    url = reverse_lazy('blog-home')



class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article.html'



def article_detail(request, pk):
    template_name = 'articles/article.html'
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, template_name, context)



class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(ArticleCreateView, self).form_valid(form)


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



class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleModelForm
    template_name = 'articles/article_update.html'



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


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog-home')




def article_delete(request, pk):
    success_url = reverse_lazy('blog-home')
    article = Article.objects.get(pk=pk)
    if request.method == 'POST' and 'delete' in request.POST:
        article.delete()
        return HttpResponseRedirect(success_url)
    else:
        return HttpResponseRedirect(article.get_absolute_url())
