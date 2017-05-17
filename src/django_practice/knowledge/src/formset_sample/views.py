from django.forms import formset_factory
from django.shortcuts import render
from django.views.generic.base import View
from django.forms import formset_factory, modelformset_factory


from .models import Schedule
from .forms import LinkForm, ScheduleModelForm


class CreateLinkView(View):
    def get(self, request, *args, **kwargs):
        LinkFormSet = formset_factory(LinkForm, extra=2)
        formset = LinkFormSet()
        context = {
            'formset': formset,
        }
        template_name = 'formset.html'
        return render(request, template_name, context)



class ScheduleInputView(View):

    template_name = 'create_schedule.html'


    def get(self, request, *args, **kwargs):
        # form
        ScheduleFormSet = modelformset_factory(Schedule, form=ScheduleModelForm)
        schedule_formset = ScheduleFormSet()

        context = {
            'schedule_formset': schedule_formset
        }

        return render(request, self.template_name, context)
