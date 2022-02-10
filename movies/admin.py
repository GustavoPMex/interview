from django.contrib import admin
from .models import MovieModel

class MovieModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(MovieModel, MovieModelAdmin)