from django.db import models
from core.core import *

# Create your models here.

LIKE_SONG_DISPLAY = ["id", "client", "track"]


class LikeSong(CoreBaseModel):
    client = models.ForeignKey('users.Client', on_delete=models.CASCADE, related_name='liked_songs')
    track = models.ForeignKey('audio.Track', on_delete=models.CASCADE, related_name='liked_by_users')



    def __str__(self):
        return self.name

    def custom_list_display():
        return LIKE_SONG_DISPLAY