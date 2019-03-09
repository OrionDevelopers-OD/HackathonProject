from . import views
from django.urls import path

app_name = 'seeds'

urlpatterns = [
    path('', views.seeds, name= 'seeds'),
]
