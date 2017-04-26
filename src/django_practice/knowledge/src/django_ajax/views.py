from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'index.html'
        context = {}
        return render(request, template_name, context)



class SignUpView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'signup.html'
        form = UserCreationForm()
        context = {
            'form': form
        }
        return render(request, template_name, context)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        return HttpResponse('posted')
