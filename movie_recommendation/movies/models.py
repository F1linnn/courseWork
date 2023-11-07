from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(max_length=200)
    slug_title = models.SlugField(unique=True, db_index=True)
    overview = models.TextField()
    keywords = models.TextField()
    production_companies = models.TextField()
    production_countries = models.TextField()
    original_language = models.CharField(max_length=20)
    genres = models.CharField(max_length=200)
    runtime= models.FloatField()
    budget = models.IntegerField()
    # release_year = models.IntegerField()
    rating = models.FloatField()
    histories = models.ForeignKey(User, blank=True, on_delete=models.DO_NOTHING)

