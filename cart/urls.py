from django.contrib import admin
from django.urls import path
from . import  views
from django.contrib.auth import  views as   auth_views


app_name = 'cart'

urlpatterns = [
    path('', views.cart_view, name= 'cart_view'),
    path('add/<int:id>/<str:model_type>/', views.cart_add, name = 'cart_add'),
    path('change/<int:id>', views.cart_change, name = 'cart_change'),
    path('delete/<int:id>', views.cart_del, name = 'cart_del'),
]
