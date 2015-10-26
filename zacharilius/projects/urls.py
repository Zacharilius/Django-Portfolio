from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
    url(r'^git-pals/', include('gitPals.urls', namespace='gitPals')),
    url(r'^$', views.index, name='index'),
)
