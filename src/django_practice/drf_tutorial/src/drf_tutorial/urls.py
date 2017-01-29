"""drf_tutorial URL Configuration

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
from snippets.api.views import SnippetViewSet, UserViewSet
from rest_framework.routers import DefaultRouter


user_list = UserViewSet.as_view(
    {
        'get': 'list'
    }
)

user_detail = UserViewSet.as_view(
    {
        'get': 'retrieve'
    }
)

router = DefaultRouter()
router.register(r'api/snippets', SnippetViewSet)
router.register(r'api/users', UserViewSet)



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    # url(r'^$', api_root),
    # url(r'^api/snippets/', include('snippets.urls')),
    # url(r'^api/users/$', user_list, name='user-list'),
    # url(r'^api/users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
