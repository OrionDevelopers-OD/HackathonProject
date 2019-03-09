from django.shortcuts import render
from django.http import HttpResponse

def garden(request):
    return render(request, "garden/garden.html")

# Create your views here.
