from django.db import models
from django.urls import reverse
from song.models import Song

# Create your models here.
class Playlist(models.Model):
    name = models.CharField(max_length=30)

    songs = models.ManyToManyField(Song)

    def get_absolute_url(self):
        return reverse("playlist_detail", kwargs={"playlist_id": self.id})

    def __str__(self):
        return self.name