from operator import imod
from django import forms
from .models import Song
from artist.models import Artist
from genre.models import Genre

class SongForm(forms.ModelForm):
    # Model form for Song 

    # Indicate this form is for the Song model and specify the fields the form will show
    class Meta:
        model = Song
        fields = [
            'name',
            'duration',
            'link',
            'artist',
            'genre',
        ]

    # Add labels to the field
    name = forms.CharField(
        label = 'Enter song title:',  
    )

    link = forms.CharField(
        label = 'Enter youtube id for this song:',
    )

    # Add an empty label (placeholder) for this field
    artist = forms.ModelChoiceField(
        queryset = Artist.objects.all(),
        empty_label = 'Choose artist',
        label = 'Artist:'
    )

    # Change the widget type for this field
    genre = forms.ModelMultipleChoiceField(
        queryset = Genre.objects.all(),
        widget = forms.CheckboxSelectMultiple(),
        label = 'Genre: (Multiple choices allowed)'
    )