from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('/category/<slug:title>/', views.product_list, name='product_list_by_category'),
    path('/product/<uuid:id>/', views.product_detail, name='product_detail'),
]
