from django.shortcuts import render
from django.http import HttpResponse

def seeds(request):
    return render(request, "Seed/seeds.html")

# Create your views here.
