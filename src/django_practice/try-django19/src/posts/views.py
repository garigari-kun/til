from django.http import HttpResponse
from django.shortcuts import render


def post_list(request):
    return HttpResponse('List')

def post_create(request):
    return HttpResponse('Create')

def post_update(request):
    return HttpResponse('Update')

def post_delete(request):
    return HttpResponse('Delete')

def post_detail(request):
    return HttpResponse('Detail')
