from django.db import models
from django.urls import reverse

# Create your models here.
class Genre(models.Model):
    # Model for Genre

    # Name field, must be unique and has max length of 30 characters
    name       = models.CharField(max_length=30, unique=True)
    # Description field, can be empty and is optional
    description = models.TextField(blank=True, null=True)
    # Field to upload image. Specifies the folder this image must be uploaded to. Also has 
    # a default image. This field is optional
    image = models.ImageField(upload_to='images/genres/', default='/images/default/placeholder.png')  

    # This field is not editable by the user, used to track how many times an genre has been clicked
    clicks = models.IntegerField(editable = False, default = 0)

    # This function returns the url leading to this genre
    def get_absolute_url(self):
        return reverse("genre_detail", kwargs={"genre_id": self.id})

    # When this object is called output the genre name
    def __str__(self):
        return self.name