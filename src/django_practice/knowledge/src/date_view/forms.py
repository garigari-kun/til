from django import forms

class ReportForm(forms.Form):
    date = forms.DateField(
        widget=forms.DateInput(attrs={
            'id': 'datepicker',
            'class': 'form-control'
        }
        )
    )
