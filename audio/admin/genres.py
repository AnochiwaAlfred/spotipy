from django.contrib import admin
from audio.models import *

# Register your models here.


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = GENRE_LIST_DISPLAY
    
    class Meta:
        verbose_name_plural = 'Genres'
