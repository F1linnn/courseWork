from django.contrib import admin
from .models import *

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug_title')
    list_display_links = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {'slug_title': ('title',)}

admin.site.register(Movie, MovieAdmin)
admin.site.register(WatchedMovie)