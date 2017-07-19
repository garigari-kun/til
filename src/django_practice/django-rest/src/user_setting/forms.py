from django import forms

from django.contrib.auth import get_user_model


class PasswordResetRequestForm(forms.Form):

    email = forms.CharField(
        label='メールアドレス',
        widget=forms.TextInput()
    )


    def clean_email(self):
        email = self.cleaned_data['email']
        user = get_user_model().objects.filter(username=email)
        if user:
            return email
        else:
            raise forms.ValidationError(
                'ユーザーは存在しません'
            )
        # try:
        #     user = get_user_model().objects.filter(username=email)
        # except:
        #     raise forms.ValidationError('ユーザーは存在しません')
        # else:
        #     return email



# http://ruddra.com/2015/09/18/implementation-of-forgot-reset-password-feature-in-django/
# https://coolors.co/326cff-5b8aff-1dad2e-747c80-a5d8ff
# https://github.com/django/django/blob/master/django/contrib/auth/views.py
# http://thinkami.hatenablog.com/entry/2016/02/17/060852
# https://docs.djangoproject.com/en/1.11/ref/contrib/messages/
# https://docs.djangoproject.com/en/1.11/topics/auth/default/
