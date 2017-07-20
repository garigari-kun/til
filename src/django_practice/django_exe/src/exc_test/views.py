from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from .forms import UserSearchForm

from django.contrib.auth import get_user_model

from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode





class UserSearchView(View):

    template_name = 'exc_test/search.html'

    def get(self, request, *args, **kwargs):
        context = {}
        context['form'] = self.get_user_search_form(request)
        return render(request, self.template_name, context)


    def post(self, request, uidb64=None, token=None, *args, **kwargs):
        context = {}
        form = self.get_user_search_form(request)
        if form.is_valid():
            UserModel = get_user_model()
            try:
                uid = urlsafe_base64_decode(uidb64)
                user = UserModel._default_manager.get(pk=uid)
            except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
                user = None

            if user is not None and default_token_generator.check_token(user, token):
                new_password= form.cleaned_data['password2']
                user.set_password(new_password)
                user.save()
            else:
                print('no user, failed token error')
        else:
            context['form'] = form
            return render(request, self.template_name, context)

    def get_user_search_form(self, request, *args, **kwargs):
        form = UserSearchForm(request.POST or None)
        return form

    def get_context_data(self, request, *args, **kwargs):
        pass



# url(r'^account/reset_password_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(),name='reset_password_confirm'),
# {{ domain }}{% url 'reset_password_confirm' uidb64=uid token=token %}
