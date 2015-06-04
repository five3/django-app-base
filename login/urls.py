from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^login', 'login.views.login'),
    url(r'^logout', 'login.views.logout'),

)
