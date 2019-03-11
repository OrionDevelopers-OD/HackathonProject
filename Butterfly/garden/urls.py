from . import views
from django.urls import path

app_name = 'garden'

urlpatterns = [
    path('', views.garden, name= 'garden'),
]
