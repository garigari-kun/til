from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from .models import Blog
from django.http import HttpResponse, Http404
from .forms import ScheduleForm
from django.contrib.auth.mixins import LoginRequiredMixin


class BlogOwnerMixin(object):
    def dispatch(self, request, id=None, *args, **kwargs):
        blog = get_object_or_404(Blog, id=id)
        if blog.user.id == request.user.id:
            return super(BlogOwnerMixin, self).dispatch(request, *args, **kwargs)
        else:
            raise Http404()




class SuperuserRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super(SuperuserRequiredMixin, self).dispatch(request, *args, **kwargs)
        else:
            raise Http404()



class BlogListView(View):

    def get(self, request, *args, **kwargs):
        template_name = 'blog/list.html'
        context = {}
        context['blog_list'] = Blog.objects.all()
        return render(request, template_name, context)



class BlogEditView(LoginRequiredMixin, BlogOwnerMixin, View):

    def get(self, request, id=None, *args, **kwargs):
        return HttpResponse('edit view')


class AdminDashboard(LoginRequiredMixin, SuperuserRequiredMixin, View):
    def get(self, request, id=None, *args, **kwargs):
        return HttpResponse('admindashboard')



class CreateScheduelFormView(View):

    def get(self, request, *args, **kwargs):
        context = {}
        context['form'] = self.get_schedule_form(request)
        return render(request, 'blog/form.html', context)

    def get_schedule_form(self, request):
        form = ScheduleForm(request.POST or None)
        return form
