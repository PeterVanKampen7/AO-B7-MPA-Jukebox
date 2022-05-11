from ftplib import all_errors
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from song.models import Song
from playlist.models import Playlist
from genre.models import Genre
from artist.models import Artist

# Create your views here.

def home_view(request, *args, **kwargs):
    # View for the home page

    # Constant that indicates how many entries the featured lists have
    FEATURED_AMOUNT = 5

    # Get all songs
    all_songs = Song.objects.all()
    # Sort songs on views DESC
    all_songs = sorted(all_songs, key = lambda x: x.views, reverse = True)
    # Get the first X amount of songs, indicated by constant
    featured_songs = all_songs[0:FEATURED_AMOUNT]

    # Get all genres
    all_genres = Genre.objects.all()
    # sort genres on clicks DESC
    all_genres = sorted(all_genres, key = lambda x: x.clicks, reverse=True)
    # Get the first X amount of genres, indicated by constant
    featured_genres = all_genres[0:FEATURED_AMOUNT]

    # Get all artists
    all_artists = Artist.objects.all()
    # Sort artists in clicks DESC
    all_artists = sorted(all_artists, key = lambda x: x.clicks, reverse=True)
    # Get the first X amount of artists, indicated by constant
    featured_artists = all_artists[0:FEATURED_AMOUNT]

    # Pass page name and featured songs, artist and genres into context
    context = {
        'page_title': 'Home',
        'songs': featured_songs,
        'genres': featured_genres,
        'artists': featured_artists,
    }

    # Render the template
    return render(request, 'home.html', context)


def user_profile_view(request):
    # View for the user profile

    # Pass page name into context
    context = {
        'page_title': f'User - {request.user}',
    }

    # Render the template
    return render(request, 'registration/profile.html', context)

def user_registration_view(request):
    # View for new user registration

    # Instantiate the form, if data for the form exists in POST pass it along
    form = UserCreationForm(request.POST or None)

    # If the form is valid create a new user with the data, log in the new user, then redirect to home page
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(request, user)
        return redirect('home')

    # Pass page name and form into context
    context = {
        'page_title': 'Registration',
        'form': form,
    }

    # Render the template
    return render(request, 'registration/registration.html', context)