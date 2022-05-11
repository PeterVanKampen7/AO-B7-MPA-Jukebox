from django import forms
from .models import Playlist

class PlaylistForm(forms.ModelForm):

    # Model form for editing and creating playlist, containing the fields name and songs

    class Meta:
        model = Playlist
        fields = [
            'name',
            'songs',
        ]