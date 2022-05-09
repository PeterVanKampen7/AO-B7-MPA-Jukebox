from django.db import models
from django.urls import reverse

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images/artists/', default='/images/default/placeholder.png')  

    clicks = models.IntegerField(editable = False, default = 0)

    def get_absolute_url(self):
        return reverse("artist_detail", kwargs={"artist_id": self.id})

    def __str__(self):
        return self.name