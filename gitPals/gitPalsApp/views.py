from django.shortcuts import render
from django.shortcuts import render

# Create your views here.

def index(request):
	context_dict = {'boldmessage': 'I am soooo bolded'}

	return render(request, 'gitPalsApp/index.html', context_dict)
