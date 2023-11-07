from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import *
from django.contrib.auth import login, authenticate
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
import csv

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

# @redirect_authenticated_user(redirect_url="/movies")
class RegisterUser(CreateView):
    form_class = RegistrationForm
    template_name = 'movies/registration_page.html'
    success_url = reverse_lazy('user_profile')

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
        return reverse_lazy('user_profile')

@login_required
def user_profile(request):
    user = request.user
    return render(request, 'movies/user_profile.html', {'user': user})

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('logout_success')
def logout_success(request):
    return redirect('/movies')

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/movie_detail.html', {'movie': movie})


@login_required
def add_to_history(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    if movie.histories is None:
        movie.histories = request.user
    # Проверяем, что текущий пользователь не добавил фильм в историю просмотра
    if movie.histories.filter(id=request.user.id).exists():
        # Пользователь уже просматривал этот фильм
        pass
    else:
        # Пользователь ещё не просматривал этот фильм, добавляем его в историю
        movie.histories.add(request.user)

    return render(request, 'movies/movie_detail.html', {'movie': movie})

def search_movies(request):
    query = request.GET.get('q', '')  # Получаем значение параметра 'q' из GET-запроса
    movies = Movie.objects.filter(title__icontains=query)  # Ищем фильмы с соответствующим заголовком
    return render(request, 'movies/movie_list.html', {'movies': movies})