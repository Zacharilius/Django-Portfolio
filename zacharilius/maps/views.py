from django.shortcuts import render
from django.http import HttpResponse

from maps.models import MushroomSpot

# Create your views here.
def index(request):
    context_dict = {'nav': 'maps'}
    return render(request, 'maps/maps.html', context_dict)

def mushroom(request):
    qs_results = MushroomSpot.objects.all()
    context_dict = {'nav': 'maps', 'qs_results': qs_results}
    return render(request, 'maps/mushroomspot_list.html', context_dict)
