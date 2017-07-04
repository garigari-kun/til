from django.http import HttpResponse
from django.shortcuts import render
from django.forms import formset_factory, modelformset_factory
from django.views.generic.base import View

from .models import Blog
from .forms import BlogDeletionCheckForm, BlogForm


class BlogMultipleDeletionView(View):

    template_name = 'blog_multiple_deletion.html'

    def get(self, request, *args, **kwargs):
        blog_articles = Blog.objects.all()
        blog_list = self.get_blog_list(request, blog_articles)
        blog_deletion_check_formset = self.get_blog_deletion_check_formset(request, extra=0, initial=blog_list)
        # blog_formset = self.get_blog_formset(request, extra=0)



        context = {
            'blog_articles': blog_articles,
            'formset': blog_deletion_check_formset,
        }
        return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        blog_articles = Blog.objects.all()
        blog_list = self.get_blog_list(request, blog_articles)
        blog_deletion_check_formset = self.get_blog_deletion_check_formset(request)
        print('blog deletion here')
        if blog_deletion_check_formset.is_valid():
            # print(blog_deletion_check_formset)
            for bdcf in blog_deletion_check_formset:
                if bdcf.cleaned_data['checkbox']:
                    print(bdcf.cleaned_data['checkbox'])
                    print(bdcf.cleaned_data['id'])
        return HttpResponse('post')



    def get_blog_deletion_check_formset(self, request, extra=0, initial=None):
        BlogDeletionCheckFormSet = formset_factory(BlogDeletionCheckForm, extra=extra)
        formset = BlogDeletionCheckFormSet(request.POST or None, initial=initial)
        return formset


    def get_blog_formset(self, request, extra=0, initial=None):
        BlogFormSet = formset_factory(BlogForm, extra=extra)
        formset = BlogFormSet(request.POST or None)
        return formset


    def get_context_data(self, request, *args, **kwargs):
        context = {}

    def get_blog_list(self, request, blog_articles):
        blog_list = []
        for blog_article in blog_articles:
            tmp_dict = {
                'id': blog_article.id,
            }
            blog_list.append(tmp_dict)

        return blog_list
