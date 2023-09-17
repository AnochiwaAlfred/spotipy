from django.db import models
from core.core import *

# Create your models here.

GENRE_LIST_DISPLAY = ["id", "name", "description"]


class Genre(CoreBaseModel):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
