from django.shortcuts import render
from django.http import HttpResponse

def plants(request):
    return render(request, "Butterfly_Plants/plants.html")

# Create your views here.
