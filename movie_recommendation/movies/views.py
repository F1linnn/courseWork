from django.shortcuts import render, redirect
from .models import Movie
from .forms import *
from django.contrib.auth import login, authenticate
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
# import csv

def movie_list(request):
    # with open('D:\Pycharm Projects\courseWork\movie_recommendation\movies\mov.csv', mode='r', encoding='utf-8') as file:
    #     # Читаем CSV-файл с помощью библиотеки csv
    #     csv_reader = csv.DictReader(file)
    #     ctr= 2
    #     for row in csv_reader:
    #         print(ctr)
    #         # Создаем объект Movie и сохраняем его в базе данных
    #         movie = Movie(
    #             title=row['title'],
    #             slug_title=row['title'].replace(" ", "_").lower(),
    #             overview=row['overview'],
    #             keywords=row['keywords'],
    #             production_companies=row['production_companies'],
    #             production_countries=row['production_countries'],
    #             original_language=row['original_language'],
    #             genres=row['genres'],
    #             runtime=row['runtime'],
    #             budget=int(row['budget']),
    #             rating=float(row['rating'])
    #         )
    #         movie.save()

    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

class RegisterUser(CreateView):
    form_class = RegistrationForm
    template_name = 'movies/registration_page.html'
    success_url = reverse_lazy('movie_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/movies')


class LoginUser(LoginView):
    form_class = LoginForm
    template_name = 'movies/auth_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('/movies')

# def registration_page(request):
#     return render(request, 'movies/registration_page.html')


# user = request.user