from django.contrib import admin

from .models import Breweries, MushroomSpot
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
admin.site.register(Breweries)
admin.site.register(MushroomSpot, LeafletGeoAdmin)
