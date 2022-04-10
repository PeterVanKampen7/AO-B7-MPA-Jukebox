from django import forms
from .models import Artist

class ArtistForm(forms.ModelForm):

    class Meta:
        model = Artist
        fields = [
            'name',
            'description',
            'age',
            'nationality',
            'image'
        ]

    # name       = forms.CharField(
    #     label = 'Enter Name:',
    #     widget = forms.TextInput(
    #             attrs= {
    #                 'placeholder': 'Pop/Rock/Jazz'
    #             }
    #         )
    #     )

    # description = forms.CharField(
    #     label = 'Enter description',
    #     widget = forms.Textarea(
    #             attrs = {
    #                 'placeholder': 'Dit is een genre van muziek...'
    #             }
    #         )
    #     )
