from django.contrib import admin
from audio.models import *

# Register your models here.


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = TRACK_LIST_DISPLAY
    list_display_links = ['title', 'id']
