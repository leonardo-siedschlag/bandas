from django.conf.urls import patterns, url
from bandasApp import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^addBandas/$', views.addBandas, name='addBandas'),)


