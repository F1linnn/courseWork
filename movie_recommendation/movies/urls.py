from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_list, name='movie_list'),
    path('registration_page/', views.RegisterUser.as_view(), name='registration_page'),
    path('auth_page/', views.LoginUser.as_view(), name='auth_page'),
]