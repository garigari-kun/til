from django import forms


from .models import Blog



class BlogDeletionCheckForm(forms.ModelForm):

    id = forms.CharField(
        widget=forms.HiddenInput()
    )

    checkbox = forms.CharField(
        widget=forms.CheckboxInput(),
        label=''
    )

    class Meta:
        model = Blog
        fields = [
            'id'
        ]


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = [
            'title',
            'content'
        ]
