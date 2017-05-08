from django.conf.urls import include, url

from .views import CreateLinkView

urlpatterns = [
    url(r'^$', CreateLinkView.as_view(), name='create-link'),

]
