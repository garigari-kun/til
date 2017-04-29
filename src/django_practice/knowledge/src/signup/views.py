from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.http import HttpResponse


class SignupView(View):

    def get(self, request, *args, **kwargs):
        template_name = 'signup2.html'
        form = UserCreationForm()
        context = {
            'form': form
        }
        return render(request, template_name, context)

    def post(self, request, *args, **kwargs):
        print('post method is called')
        form  = UserCreationForm(request.POST)
        if form.is_valid():
            print('valid form')
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponse('Login')
        else:
            template_name = 'signup2.html'
            context = {
                'form': form
            }
            return render(request, template_name, context)
