from django.db import models
from core.core import *
from plugins.generate_filename import generate_filename

# Create your models here.

PLAYLIST_LIST_DISPLAY = [
    "id",
    "title",
    "description",
    "client",
]


class Playlist(CoreBaseModel):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    tracks = models.ManyToManyField(
        "audio.Track",
        blank=True,
        related_name="playlistTracks",
    )
    client = models.ForeignKey(
        "users.Client",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="playlistOwner",
    )

    def __str__(self):
        return self.title
