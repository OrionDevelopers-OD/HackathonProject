from . import views
from django.urls import path

urlpatterns = [
    path('', views.about1, name='about1')
]
