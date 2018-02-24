# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from . import views

from django.contrib import admin

admin.autodiscover()

urlpatterns =  [
    url(r'^$', views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^saleslist/', views.saleslist, name='saleslist'),
    url(r'^prognoz/$', views.prognoz, name='prognoz'),
    url(r'^upload/', views.upload, name="upload"),
    url(r'^select_prognoz/', views.select_prognoz, name="select_prognoz"),
    url(r'^select/', views.select, name="select"),
]
