from django import forms

from django.contrib.auth import get_user_model



class UserSearchForm(forms.Form):

    username = forms.CharField(
        max_length=64,
        label='ユーザー名',
        widget=forms.TextInput()
    )


    def clean_username(self):
        klass = get_user_model()
        username = self.cleaned_data['username']
        try:
            user_instance = klass._default_manager.get(username=username)
        except klass.DoesNotExist:
            raise forms.ValidationError('ユーザーは存在しません')
        return username
