from django.db import models
from core.core import CoreBaseModel
from users.models import CustomUser
from plugins.generate_filename import generate_filename


FOLLOWER_DISPLAY = ['id', 'follower', 'followed']
class Follower(CoreBaseModel):
    follower = models.ForeignKey('users.Client', on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey('users.Artist', on_delete=models.CASCADE, related_name='followers')

    class Meta:
        verbose_name = "Follower"
        verbose_name_plural = "Followers"

    def __str__(self):
        return f"{self.follower} --> {self.followed}"

    def custom_list_display():
        return FOLLOWER_DISPLAY