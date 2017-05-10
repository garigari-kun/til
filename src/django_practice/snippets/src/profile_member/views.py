from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from .models import Profile, FamilyMember
from .forms import FamilyMemberForm, FamilyMemberFormSet


class ProfileList(ListView):
    model = Profile



class ProfileFamilyMemberCreate(CreateView):
    model = Profile
    fields = ['first_name', 'last_name']
    # success_url = reverse_lazy('profile-list')
    template_name = 'profile_form.html'

    def get_context_data(self, **kwargs):
        data = super(ProfileFamilyMemberCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['familymembers'] = FamilyMemberFormSet(self.request.POST)
        else:
            data['familymembers'] = FamilyMemberFormSet()
        return data


    def form_valid(self, form):
        context = self.get_context_data()
        familymembers = context['familymembers']
        with transaction.atomic():
            self.object = form.save()

            if familymembers.is_valid():
                familymembers.instance = self.object
                familymembers.save()
        return super(ProfileFamilyMemberCreate, self).form_valid(form)
