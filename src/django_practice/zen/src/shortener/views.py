from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import ZenURL


def zen_redirect_view(request, shortcode=None, *args, **kwargs):
    obj = get_object_or_404(ZenURL, shortcode=shortcode)
    return HttpResponse('hello')


class ZenCBView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(ZenURL, shortcode=shortcode)
        # return HttpResponse('hello again')
        return HttpResponseRedirect(obj.url)
