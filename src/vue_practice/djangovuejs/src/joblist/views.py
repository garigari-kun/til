from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.shortcuts import render

from rest_framework import viewsets

from .models import JobList
from .serializers import JobListSerializer


def job_list(request):
    template_name = 'joblist.html'
    context = {
        'jobs': JobList.objects.all()
    }
    html = TemplateResponse(request, template_name, context)
    # return HttpResponse(html)
    return render(request, template_name, context)

class JobListViewSet(viewsets.ModelViewSet):
    queryset = JobList.objects.all()
    serializer_class = JobListSerializer
