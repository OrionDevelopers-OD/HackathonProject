from . import views
from django.urls import path

app_name = 'cart'

urlpatterns = [
    path('', views.cart, name= 'cart'),
]
