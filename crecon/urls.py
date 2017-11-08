# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include, url
from . import views

from django.contrib import admin

from filebrowser.sites import site

admin.autodiscover()

urlpatterns =  [
    url(r'^$', views.base, name='base'),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
