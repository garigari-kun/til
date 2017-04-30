from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('IndexView called')
