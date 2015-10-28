from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    context_dict = {'nav': 'maps'}
    return render(request, 'maps/maps.html', context_dict)
