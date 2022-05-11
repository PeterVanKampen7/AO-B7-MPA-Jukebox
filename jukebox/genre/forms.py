from django import forms
from .models import Genre

class GenreForm(forms.ModelForm):

    # Model form for updating and creating a Genre
    
    # Define the fields that will show up in the form
    class Meta:
        model = Genre
        fields = [
            'name',
            'description',
            'image',
        ]

    # Give the fields extra customizable options, like labels
    name       = forms.CharField(
        label = 'Enter Name:',
        widget = forms.TextInput(
                attrs= {
                    'placeholder': 'Pop/Rock/Jazz'
                }
            )
        )

    description = forms.CharField(
        label = 'Enter description',
        widget = forms.Textarea(
                attrs = {
                    'placeholder': 'Dit is een genre van muziek...'
                }
            )
        )
