from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_list, name='movie_list'),
    path('registration_page/', views.RegisterUser.as_view(), name='registration_page'),
    path('auth_page/', views.LoginUser.as_view(), name='auth_page'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('custom_logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('logout_success/', views.logout_success, name='logout_success'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('search/', views.search_movies, name='search_movies'),

]