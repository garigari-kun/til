from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.base import TemplateView, View
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.forms import formset_factory, modelformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import EventModelForm, ScheduleModelForm
from .models import Event, Schedule
# Create your views here.
class UpdateEventView(View):

    template_name = 'create_event.html'

    def get(self, request, pk=None, *args, **kwargs):
        event = get_object_or_404(Event, pk=pk)
        event_form = self.get_event_form(request, instance=event)
        schedule_list = []
        for schedule in event.schedule_range.all():
            dictio = {
                'date': schedule.date,
                'comment': schedule.comment
            }
            print(dictio)
            schedule_list.append(dictio)
        print(schedule_list)

        schedule_formset = self.get_schedule_formset(request, instance=schedule_list)
        # schedule_formset = self.get_schedule_formset(request, instance=schedule_list)

        context = {
            'event_form': event_form,
            'schedule_formset': schedule_formset
        }
        return render(request, self.template_name, context)

        # return HttpResponse('update view')

    def post(self, request, event_code=None, *args, **kwargs):
        pass

    def get_event_form(self, request, instance, *args, **kwargs):
        form = EventModelForm(request.POST or None, instance=instance)
        return form

    def get_schedule_formset(self, request, extra=0, instance=None, *args, **kwargs):
        ScheduleFormSet = formset_factory(ScheduleModelForm, extra=0)
        formset = ScheduleFormSet(request.POST or None, initial=instance)

        return formset
