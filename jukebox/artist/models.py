from django.db import models
from django.urls import reverse

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    age = models.IntegerField()
    nationality = models.CharField(max_length=30)

    def get_absolute_url(self):
        return reverse("artist_detail", kwargs={"artist_id": self.id})