from django.db import models
from django.urls import reverse
from song.models import Song
from django.contrib.auth.models import User

# Create your models here.

class Playlist(models.Model):
    # Model for a playlist

    # Name of the playlist, max length of 30 characters
    name = models.CharField(max_length=30)
    # Assign the playlist to a user
    # When playlist is deleted do not delete user
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    # Add many to many Song relation
    songs = models.ManyToManyField(Song)

    # This function returns the url leading to this playlist
    def get_absolute_url(self):
        return reverse("playlist_detail", kwargs={"playlist_id": self.id})

    # When this object is called output the playlist name
    def __str__(self):
        return self.name

    # Set user for this playlist, user is passed as parameter
    def set_user(self, user):
        self.user = user
        self.save() 