from datetime import timedelta
from django.db import models
from django.utils import timezone
from django.urls import reverse

from artist.models import Artist
from genre.models import Genre


# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length=30)
    link = models.CharField(max_length=11)
    duration = models.DurationField(default=timedelta(days=0,seconds=0,microseconds=0))

    views = models.IntegerField(default=0, editable=False)
    dateAdded = models.DateField(default=timezone.now, editable=False) 

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)

    def get_absolute_url(self):
        return reverse("song_detail", kwargs={"song_id": self.id})

    def __str__(self):
        return self.name