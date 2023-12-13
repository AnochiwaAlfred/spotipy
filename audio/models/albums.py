from django.db import models
from core.core import *
from plugins.generate_filename import generate_filename

# Create your models here.

ALBUM_LIST_DISPLAY = ["id", "title", "artist", "genre", "releaseDate"]


class Album(CoreBaseModel):
    title = models.CharField(max_length=100, blank=True, null=True)
    artist = models.ForeignKey(
        "users.Artist",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="albumArtist",
    )
    genre = models.ForeignKey(
        "audio.Genre",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="albumGenre",
    )
    tracks = models.ManyToManyField(
        "audio.Track", blank=True, related_name="albumTracks"
    )
    releaseDate = models.DateField(blank=True, null=True)
    coverArt = models.ImageField(null=True, blank=True, upload_to=generate_filename)

    def get_duration(self):
        return "200 Minutes"

    def __str__(self):
        return self.title
    
    def custom_list_display():
        return ALBUM_LIST_DISPLAY
