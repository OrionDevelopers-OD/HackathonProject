from . import views
from django.urls import path

app_name = 'plants'

urlpatterns = [
    path('', views.plants, name= 'plants'),
]
