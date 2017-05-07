from django.forms import formset_factory
from django.shortcuts import render
from django.views.generic.base import View

from .forms import LinkForm


class CreateLinkView(View):
    def get(self, request, *args, **kwargs):
        LinkFormSet = formset_factory(LinkForm)
        formset = LinkFormSet()
        context = {
            'formset': formset,
        }
        template_name = 'formset.html'
        return render(request, template_name, context)
