from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    context_dict = {'boldmessage': 'I am bolded'}
    return render(request, 'projects/projects.html', context_dict)