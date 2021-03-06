from django.db import models
from djgeojson.fields import PointField

# Create your models here.
class Breweries(models.Model):
    title = models.CharField("title", max_length=128)
    longitude = models.FloatField("longitude")
    latitude = models.FloatField("latitude")
    streetAddress = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    state = models.CharField(max_length=128)
    url = models.URLField()
    
    def __unicode__(self):
        return self.title
    
class MushroomSpot(models.Model):
    geom = PointField()
    description = models.TextField()
    picture = models.ImageField()

    @property
    def popupContent(self):
      return '<img src="{}" /><p><{}</p>'.format(
          self.picture.url,
          self.description)