from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404, render, get_list_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Playlist
from .forms import PlaylistForm
from song.models import Song

# Create your views here.

@login_required
# Login required for this page
def playlist_add_view(request):
    # Create the view for adding a playlist

    # Instantiate the form, if data for the form exists in POST pass them along
    form = PlaylistForm(request.POST or None)

    # If the submitted form is valid save the playlist, add the current user as owner and redirect to playlist list page
    if form.is_valid():
        playlist = form.save()
        playlist.set_user(request.user)
        return redirect('/playlist')

    # Pass page name and form into context
    context = {
        'page_title': 'Add playlist',
        'form': form,
    }

    # Render the template
    return render(request, 'playlist/playlist_add.html', context)

@login_required
# Login required for this page
def playlist_list_view(request):
    # Create the view for the playlist list view

    # Get all playlists
    queryset = Playlist.objects.all()

    # Create empty array to fill with the playlist belonging to current user
    user_playlists = []
    # Loop through all playlists
    for playlist in queryset:
        # If this playlist belongs to the current user add it to the array
        if playlist.user == request.user:
            user_playlists.append(playlist)

    # Pass page name and the users playlists into context
    context = {
        'page_title': 'All playlists',
        'object_list': user_playlists,
    }

    # Render the template
    return render(request, 'playlist/playlist_list.html', context)

def playlist_detail_view(request, playlist_id):
    # Create the view for the playlist detail view

    # Get the playlist with the id passed in the URL through the route
    obj = get_object_or_404(Playlist, id=playlist_id)

    # Create empty timedelta to store total playlist duration in
    duration = timedelta()
    # Loop through all songs in this playlist and add the duration of the song into the timedelta
    for song in obj.songs.all():
        duration += song.duration

    # If the current user does not match the user of this playlist redirect to home
    if obj.user != request.user:
        return redirect('/')

    # If the form to delete a song from this playlist is submitted remove the song from the playlist and refresh the page
    if request.GET.get('removed_song', '') and request.GET.get('playlist_id', ''):
        obj.songs.remove(request.GET.get('removed_song', ''))
        obj.save()
        return redirect(f'/playlist/{obj.id}')

    # If the form to add a song to this playlist is submitted add the song to the playlist and refresh the page
    if request.GET.get('new_song', ''):
        obj.songs.add(get_object_or_404(Song, id=request.GET.get('new_song', '')))
        obj.save()
        return redirect(f'/playlist/{obj.id}')

    # Pass page name, the playlist, the playlist duration and all songs into context
    context = {
        'page_title': f"Playlist - {obj.name}",
        'object': obj,
        'full_duration': duration,
        'songs': Song.objects.all(),
    }

    # Render the template
    return render(request, 'playlist/playlist_detail.html', context)

@login_required
# Login is required for this view
def playlist_edit_view(request, playlist_id):
    # Create the view to edit a playlist

    # Get the playlist with the id in the URL passed through the route
    obj = get_object_or_404(Playlist, id=playlist_id)  

    # Instantiate the form, if data for the form exists in POST pass them along, pass current obj as well to fill form with existing data
    form = PlaylistForm(request.POST or None, instance=obj)
    # If the submitted form is valid save the form and redirect to playlist list page
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('/playlist')
    
    # Pass page name and form into context
    context = {
        'page_title': f"Edit playlist - {obj.name}",
        'form': form
    }

    # Render the template
    return render(request, 'playlist/playlist_add.html', context)

def playlist_delete_view(request, playlist_id):
    # Create the view to delete a playlist

    # Get the playlist with the id in the URL passed through the route
    obj = get_object_or_404(Playlist, id=playlist_id)  

    # If the delete form was submitted delete the playlist and redirect to playlist list page
    if request.method == 'POST':
        obj.delete()
        return redirect('/playlist')

    # Pass page name and playlist into context
    context = {
        'page_title': f"Delete playlist - {obj.name}",
        'object': obj,
    }

    # Render the template
    return render(request, 'playlist/playlist_delete.html', context)