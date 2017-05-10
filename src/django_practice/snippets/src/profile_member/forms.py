from django import forms
from django.forms.models import inlineformset_factory

from .models import Profile, FamilyMember


class FamilyMemberForm(forms.ModelForm):
    class Meta:
        model = FamilyMember
        exclude = ()


FamilyMemberFormSet = inlineformset_factory(Profile, FamilyMember, form=FamilyMemberForm, extra=1)
