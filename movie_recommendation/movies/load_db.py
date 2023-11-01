import csv
from models import Movie
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_recommendation.settings')
django.setup()
# Открываем CSV-файл для чтения
with open('mov.csv', mode='r', encoding='utf-8') as file:
    # Читаем CSV-файл с помощью библиотеки csv
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        # Создаем объект Movie и сохраняем его в базе данных
        movie = Movie(
            title=row['title'],
            # slug_title=row['title'],
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
        break