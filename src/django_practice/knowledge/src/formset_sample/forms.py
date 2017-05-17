from django import forms
#from django.forms.formsets import inlineformset_factory

from .models import Profile, FamilyMember, Schedule


class LinkForm(forms.Form):
    anchor = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Link Name / Anchor name'
            }
        ),
        required=False
    )

    url = forms.URLField(
        widget=forms.URLInput(
            attrs={
                'placeholder': 'URL'
            }
        ),
        required=False
    )



class FamilyMemberForm(forms.ModelForm):
    class Meta:
        model = FamilyMember
        exclude = ()

# FamilyMemberFormSet = inlineformset_factory(Profile, FamilyMember,
#                                             form=FamilyMemberForm, extra=1)



class ScheduleModelForm(forms.ModelForm):

    date = forms.DateField(
        label='',
        widget=forms.DateInput(attrs={
            'placeholder': '日付',
            'class': 'form-control'
        })
    )

    comment = forms.CharField(
        max_length=120,
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': '時間、一言メモ',
            'class': 'form-control'
        })
    )

    class Meta:
        model = Schedule
        fields = [
            'date',
            'comment',
        ]
