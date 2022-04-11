from django.db import models
from django.forms import CharField
from artist.models import Artist
from genre.models import Genre

from django.utils import timezone

# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length=30)
    link = models.URLField(max_length=200)
    views = models.IntegerField(default=0, editable=False)
    dateAdded = models.DateField(default=timezone.now, editable=False)

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
