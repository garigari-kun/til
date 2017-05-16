from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=64,
        required=True,
        label='お名前'
    )
    mail = forms.EmailField(
        required=True,
        label='メールアドレス'
    )
    content = forms.CharField(
        max_length=1200,
        widget=forms.Textarea(),
        required=True,
        label='内容'
    )
