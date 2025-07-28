from django.contrib import admin
from django.urls import path
from . import  views
from django.contrib.auth import  views as   auth_views


app_name = 'shop'

urlpatterns = [
    path('list/', views.ListProducts.as_view(), name='list_of_products'),
    path('list/category/<str:title>/', views.ListProductsByCategory.as_view(), name='list_by_category'),
    path('detail/<slug:slug>', views.ProductDetail.as_view(), name='product_detail')
]
