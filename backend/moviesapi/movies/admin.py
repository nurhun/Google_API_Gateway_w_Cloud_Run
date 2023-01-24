from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # list_display = ('id', 'title')
    list_display = [field.name for field in Movie._meta.get_fields()]
