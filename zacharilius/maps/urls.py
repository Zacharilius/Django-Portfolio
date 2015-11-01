from django.conf.urls import patterns, url
from djgeojson.views import GeoJSONLayerView

from . import views
from .models import MushroomSpot

urlpatterns = patterns('',
    url(r'^data.geojson$', GeoJSONLayerView.as_view(model=MushroomSpot), name='data'),
    url(r'^mushrooms/', views.mushroom, name='mushrooom'),
    url(r'^$', views.index, name='index'),
)
