from django import forms
#from django.forms.formsets import inlineformset_factory

from .models import Profile, FamilyMember


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
