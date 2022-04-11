from operator import imod
from django import forms
from .models import Song
from artist.models import Artist
from genre.models import Genre

class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = [
            'name',
            'link',
            'artist',
            'genre',
        ]

    name = forms.CharField(
        label = 'Enter song title:',  
    )

    link = forms.CharField(
        label = 'Enter youtube id for this song:',
    )

    artist = forms.ModelChoiceField(
        queryset = Artist.objects.all(),
        empty_label = 'Choose artist',
        label = 'Artist:'
    )

    genre = forms.ModelMultipleChoiceField(
        queryset = Genre.objects.all(),
        widget = forms.CheckboxSelectMultiple(),
        label = 'Genre: (Multiple choices allowed)'
    )