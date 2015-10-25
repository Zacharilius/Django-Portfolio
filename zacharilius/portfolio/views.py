from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    context_dict = {'boldmessage': 'I am bolded'}
    return render(request, 'portfolio/index.html', context_dict)