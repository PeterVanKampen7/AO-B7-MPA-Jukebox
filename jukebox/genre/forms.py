from django import forms
from .models import Genre

class GenreForm(forms.ModelForm):

    class Meta:
        model = Genre
        fields = [
            'name',
            'description'
        ]

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
