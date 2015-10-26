from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
    url(r'^projects/', include('projects.urls', namespace='projects')),
    url(r'^maps/', include('maps.urls', namespace='maps')),
    url(r'^$', views.index, name='index'),
)
