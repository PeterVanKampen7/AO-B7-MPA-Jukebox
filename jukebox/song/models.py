from datetime import timedelta
from django.db import models
from django.utils import timezone
from django.urls import reverse

from artist.models import Artist
from genre.models import Genre


# Create your models here.
class Song(models.Model):
    # Model for a song

    # Name field with a max lenght of 30 characters
    name = models.CharField(max_length=30)
    # This field contains the youtube id of this song, these id's are 11 characters long so that is also the max length of this field
    link = models.CharField(max_length=11)
    # Duration field for how much time this song takes
    duration = models.DurationField(default=timedelta(days=0,seconds=0,microseconds=0))

    # Non user editable field that tracks the amount of views this song has had
    views = models.IntegerField(default=0, editable=False)
    # Non user editable field that contains the date this song was added, defaults to current datetime and is not edited anywhere else
    dateAdded = models.DateField(default=timezone.now, editable=False) 

    # Many to One relation to Artist
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    # Many to Many relation to Genre
    genre = models.ManyToManyField(Genre)

    # This function returns the url leading to this Song
    def get_absolute_url(self):
        return reverse("song_detail", kwargs={"song_id": self.id})

    # When this object is called output the song name
    def __str__(self):
        return self.name