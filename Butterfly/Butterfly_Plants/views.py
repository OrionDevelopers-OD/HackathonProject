from django.shortcuts import render

def plants(request):
    return render(request, "Plants/plants.html")

# Create your views here.
