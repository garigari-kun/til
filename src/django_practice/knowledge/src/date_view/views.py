from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

from .forms import ReportForm



class ReportView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'report.html'
        form = ReportForm()
        context = {
            'form': form
        }
        return render(request, template_name, context)


    def post(self, request, *args, **kwargs):
        form = ReportForm(request.POST or None)
        if form.is_valid():
            date = form.cleaned_data['date']
            year = date.year
            month = format(date, 'm')
            print(month)
            day = date.day

        return HttpResponse('post has been posted')


class ReportDetailView(View):
    def get(self, request, *args, **kwargs):
        pass
