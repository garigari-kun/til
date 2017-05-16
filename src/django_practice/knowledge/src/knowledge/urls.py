"""knowledge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^django_ajax/', include('django_ajax.urls', namespace='da')),
    url(r'^date_view/', include('date_view.urls', namespace='dv')),
    url(r'^signup/', include('signup.urls', namespace='su')),
    url(r'^hosts_sample/', include('hosts_sample.urls', namespace='hs')),
    url(r'^formset_sample/', include('formset_sample.urls', namespace='fs')),
]