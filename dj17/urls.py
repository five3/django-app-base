from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^$', 'dj17.views.index', name='index'),
    url(r'^login/', include('login.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
