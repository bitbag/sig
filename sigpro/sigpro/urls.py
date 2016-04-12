"""sigpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from sigtask.views import index, basex, CreateMission, WriteToRedis, GetFromRedis
from sigtask.views import MusicianViewset, AlbumViewset, ServicesViewset
from rest_framework import routers
from rest_framework.authtoken import views as restview

router = routers.DefaultRouter()
router.register(r'musican',MusicianViewset)
router.register(r'album',AlbumViewset)
router.register(r'service',ServicesViewset)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/token/', restview.obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
    url(r'^index/', index),
    url(r'^basex/', basex),
    url(r'^createmission/', CreateMission),
    url(r'^rewis/', WriteToRedis),
    url(r'^redis/', GetFromRedis),
]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
