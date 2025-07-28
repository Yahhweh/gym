from django.contrib import admin
from django.urls import path
from . import  views


app_name = 'listofgyms'

urlpatterns = [
    path('', views.GymList.as_view(), name='gym_list'),
    path('<int:pk>/', views.GymDetail.as_view(), name='gym_detail'),
]
