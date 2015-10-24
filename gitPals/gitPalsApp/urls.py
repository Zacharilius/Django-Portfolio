from django.conf.urls import patterns, url

from gitPalsApp import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
)
