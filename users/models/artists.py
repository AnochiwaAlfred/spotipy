from django.db import models
from users.models import CustomUser
from plugins.generate_filename import generate_filename


class Artist(CustomUser):
    image = models.ImageField(null=True, blank=True, upload_to=generate_filename)
    coverImage = models.ImageField(null=True, blank=True, upload_to=generate_filename)
    bio = models.CharField(max_length=1000, null=True, blank=True)
    stageName = models.CharField(max_length=300, null=True, blank=True)

    class Meta:
        verbose_name = "Artist"
        verbose_name_plural = "Artists"

    def __str__(self):
        return self.username
