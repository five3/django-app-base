from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^$', 'dj17.views.home', name='home'),
    url(r'^account/', include('login.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
