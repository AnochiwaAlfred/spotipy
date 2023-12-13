from django.contrib import admin
from audio.models import *

# Register your models here.


@admin.register(LikeSong)
class LikeSongAdmin(admin.ModelAdmin):
    list_display = LIKE_SONG_DISPLAY

    class Meta:
        verbose_name_plural = 'Like Songs'