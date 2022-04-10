from django.db import models
from django.urls import reverse

# Create your models here.
class Genre(models.Model):
    name       = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/genres/', default='/static/img/placeholder.png')  

    def get_absolute_url(self):
        return reverse("genre_detail", kwargs={"genre_id": self.id})