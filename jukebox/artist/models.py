from django.db import models
from django.urls import reverse

# Create your models here.
class Artist(models.Model):
    # Model for an artist.

    # Name field, this field must be unique and has a max length of 30 characters 
    name = models.CharField(max_length=30, unique=True)
    # Description field, has no max lenght
    description = models.TextField()
    # Field to upload image. Specifies the folder this image must be uploaded to. Also has 
    # a default image. This field is optional
    image = models.ImageField(upload_to='images/artists/', default='/images/default/placeholder.png')  

    # This field is not editable by the user, used to track how many times an artist has been clicked
    clicks = models.IntegerField(editable = False, default = 0)

    # This function returns the url leading to this artist
    def get_absolute_url(self):
        return reverse("artist_detail", kwargs={"artist_id": self.id})

    # When this object is called output the artist name
    def __str__(self):
        return self.name