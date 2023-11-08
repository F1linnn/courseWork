from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import WatchedMovie
from .forms import *
from django.contrib.auth import login, authenticate
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
# from .alg_recommendation import recommend_movies
# import csv

def movie_list(request):
   

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

# @login_required
# # def user_profile(request):
# #     user = request.user
# #     return render(request, 'movies/user_profile.html', {'user': user})

@login_required
def user_profile(request):
    user = request.user
    watched_movies = WatchedMovie.objects.filter(user=user)
    return render(request, 'movies/user_profile.html', {'user': user, 'watched_movies': watched_movies})

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

    if request.method == 'POST':
        rating = request.POST.get('rating')  # Получаем рейтинг из запроса

        if rating and rating.isdigit():
            rating = int(rating)
            if 1 <= rating <= 10:
                if not WatchedMovie.objects.filter(user=request.user, movie=movie).exists():
                    WatchedMovie.objects.create(user=request.user, movie=movie, rating=int(rating))
                else:
                    history = WatchedMovie.objects.get(user=request.user, movie=movie)
                    history.rating = rating
                    history.save()
    return render(request, 'movies/movie_detail.html', {'movie': movie})

def search_movies(request):
    query = request.GET.get('q', '')  # Получаем значение параметра 'q' из GET-запроса
    movies = Movie.objects.filter(title__icontains=query)  # Ищем фильмы с соответствующим заголовком
    return render(request, 'movies/movie_list.html', {'movies': movies})


def get_recommendations(request):
    n_recommendations = 5  # Количество рекомендаций, которое вы хотите вернуть
    recommended_movies = recommend_movies(request.user.id, n_recommendations)

    movie_data = [{'title': movie.title, 'overview': movie.overview} for movie in recommended_movies]

    return JsonResponse({'recommendations': movie_data})