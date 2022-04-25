from django.db import models
from django.urls import reverse
from song.models import Song
from django.contrib.auth.models import User

# Create your models here.
class Playlist(models.Model):
    name = models.CharField(max_length=30)

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)

    songs = models.ManyToManyField(Song)

    def get_absolute_url(self):
        return reverse("playlist_detail", kwargs={"playlist_id": self.id})

    def __str__(self):
        return self.name

    def set_user(self, user):
        self.user = user
        self.save()