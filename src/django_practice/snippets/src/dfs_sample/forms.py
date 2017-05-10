from django import forms


class DateDetailForm(forms.Form):
    date = forms.CharField(max_length=10, widget=forms.DateInput())
    memo = forms.CharField(max_length=100, widget=forms.TextInput())
