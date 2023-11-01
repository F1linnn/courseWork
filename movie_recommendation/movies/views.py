from django.shortcuts import render
from .models import Movie
import csv

def movie_list(request):
    print(0)
    with open('D:\Pycharm Projects\courseWork\movie_recommendation\movies\mov.csv', mode='r', encoding='utf-8') as file:
        # Читаем CSV-файл с помощью библиотеки csv
        csv_reader = csv.DictReader(file)
        ctr= 2
        for row in csv_reader:
            print(ctr)
            # Создаем объект Movie и сохраняем его в базе данных
            movie = Movie(
                title=row['title'],
                slug_title=row['title'].replace(" ", "_").lower(),
                overview=row['overview'],
                keywords=row['keywords'],
                production_companies=row['production_companies'],
                production_countries=row['production_countries'],
                original_language=row['original_language'],
                genres=row['genres'],
                runtime=row['runtime'],
                budget=int(row['budget']),
                rating=float(row['rating'])
            )
            movie.save()

    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})


def load_db(request):

        return render(request, 'movies/movie_list.html')
