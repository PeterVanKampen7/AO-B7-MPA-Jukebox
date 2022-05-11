from django import forms
from .models import Artist

class ArtistForm(forms.ModelForm):

    # Model form for the creation and editing of an artist. 
    # Includes the name, description and image fields for the user to fill in

    class Meta:
        model = Artist
        fields = [
            'name',
            'description',
            'image'
        ]