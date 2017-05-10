from django.shortcuts import render
from django.forms import formset_factory
from django.views.generic.base import View

from .forms import DateDetailForm



class CreateDateView(View):

    def get(self, request, *args, **kwargs):
        template_name = 'create.html'
        #form = DateDetailForm()
        FormSet = formset_factory(DateDetailForm, extra=1)
        form = FormSet()
        context = {
            'form': form
        }
        return render(request, template_name, context)
