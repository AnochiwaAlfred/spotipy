from django.db import models
from core.core import *
from plugins.generate_filename import generate_filename

# Create your models here.

TRACK_LIST_DISPLAY = [
    "id",
    "title",
    "playCount",
    "releaseDate",
    "artist",
    "genre",
]


class Track(CoreBaseModel):
    title = models.CharField(max_length=100, blank=True, null=True)
    lyrics = models.TextField(blank=True, null=True, default="")
    playCount = models.IntegerField(null=True, blank=True, default=0)
    releaseDate = models.DateField(blank=True, null=True)
    artist = models.ForeignKey(
        "users.Artist",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="trackArtist",
    )
    correspondingArtists = models.ManyToManyField(
        "users.Artist",
        blank=True,
        related_name="correspondingArtist",
    )
    genre = models.ForeignKey(
        "audio.Genre",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="trackGenre",
    )
    audioFile = models.FileField(upload_to="audio_files", null=True, blank=True)
    coverImage = models.ImageField(null=True, blank=True, upload_to=generate_filename)
    # likes = models.ManyToManyField('users.Client', related_name='liked_tracks', blank=True)
    def get_duration(self):
        return "200 Minutes"

    def __str__(self):
        return self.title
