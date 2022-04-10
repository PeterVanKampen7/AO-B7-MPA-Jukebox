from django.db import models
from django.urls import reverse

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    age = models.IntegerField()
    nationality = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/artists/', default='/images/default/placeholder.png')  

    def get_absolute_url(self):
        return reverse("artist_detail", kwargs={"artist_id": self.id})