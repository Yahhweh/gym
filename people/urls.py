from django.contrib import admin
from django.urls import path
from . import  views
from django.contrib.auth import  views as   auth_views


app_name = 'people'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(next_page= 'listofgyms:gym_list'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page = 'listofgyms:gym_list'), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('client_profile/', views.ProfileView.as_view(), name='client_profile'),
    path('trainer/<int:pk>/', views.DetailTrainers.as_view(), name='trainer')
]
