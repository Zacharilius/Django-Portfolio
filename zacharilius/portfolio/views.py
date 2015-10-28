from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    context_dict = {'nav': 'home'}
    return render(request, 'portfolio/index.html', context_dict)