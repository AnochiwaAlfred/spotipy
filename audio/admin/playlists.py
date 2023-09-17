from django.contrib import admin
from audio.models import *

# Register your models here.


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = PLAYLIST_LIST_DISPLAY
