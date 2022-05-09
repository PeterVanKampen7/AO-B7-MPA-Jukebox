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

    FEATURED_AMOUNT = 5

    all_songs = Song.objects.all()
    all_songs = sorted(all_songs, key = lambda x: x.views, reverse = True)
    featured_songs = all_songs[0:FEATURED_AMOUNT]

    all_genres = Genre.objects.all()
    all_genres = sorted(all_genres, key = lambda x: x.clicks, reverse=True)
    featured_genres = all_genres[0:FEATURED_AMOUNT]

    all_artists = Artist.objects.all()
    all_artists = sorted(all_artists, key = lambda x: x.clicks, reverse=True)
    featured_artists = all_artists[0:FEATURED_AMOUNT]

    context = {
        'page_title': 'Home',
        'songs': featured_songs,
        'genres': featured_genres,
        'artists': featured_artists,
    }

    return render(request, 'home.html', context)


def user_profile_view(request):

    context = {
        'page_title': f'User - {request.user}',
    }

    return render(request, 'registration/profile.html', context)

def user_registration_view(request):

    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(request, user)
        return redirect('home')

    context = {
        'page_title': 'Registration',
        'form': form,
    }

    return render(request, 'registration/registration.html', context)