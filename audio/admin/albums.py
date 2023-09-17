from django.contrib import admin
from audio.models import *

# Register your models here.


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ALBUM_LIST_DISPLAY
