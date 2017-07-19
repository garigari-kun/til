from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

from .forms import PasswordResetRequestForm


class PasswordResetRequestView(View):

    def get(self, request, *args, **kwargs):
        template_name = self.get_template_name(request)
        context = self.get_context_data(request)
        return render(request, template_name, context)


    def post(self, request, *args, **kwargs):
        form = self.get_password_reset_request_form(request)
        if form.is_valid():
            print('form valid')
            return HttpResponse('post valid')

        template_name = self.get_template_name(request)
        context = self.get_context_data(request)
        return render(request, template_name, context)


    def get_template_name(self, request):
        template_name = 'user_setting/forgot_password.html'
        return template_name


    def get_context_data(self, request):
        context = {}
        context['p_r_form'] = self.get_password_reset_request_form(request)
        return context


    def get_password_reset_request_form(self, request):
        form = PasswordResetRequestForm(request.POST or None)
        return form
