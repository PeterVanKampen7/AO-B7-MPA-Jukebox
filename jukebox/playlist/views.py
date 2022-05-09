from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404, render, get_list_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Playlist
from .forms import PlaylistForm
from song.models import Song

# Create your views here.
@login_required
def playlist_add_view(request):
    form = PlaylistForm(request.POST or None)

    if form.is_valid():
        playlist = form.save()
        playlist.set_user(request.user)
        return redirect('/playlist')

    context = {
        'page_title': 'Add playlist',
        'form': form,
    }

    return render(request, 'playlist/playlist_add.html', context)

@login_required
def playlist_list_view(request):
    queryset = Playlist.objects.all()

    user_playlists = []
    for playlist in queryset:
        if playlist.user == request.user:
            user_playlists.append(playlist)

    context = {
        'page_title': 'All playlists',
        'object_list': user_playlists,
    }

    return render(request, 'playlist/playlist_list.html', context)

def playlist_detail_view(request, playlist_id):
    obj = get_object_or_404(Playlist, id=playlist_id)

    duration = timedelta()
    for song in obj.songs.all():
        duration += song.duration

    if obj.user != request.user:
        return redirect('/')

    if request.GET.get('removed_song', '') and request.GET.get('playlist_id', ''):
        obj.songs.remove(request.GET.get('removed_song', ''))
        obj.save()
        return redirect(f'/playlist/{obj.id}')

    if request.GET.get('new_song', ''):
        obj.songs.add(get_object_or_404(Song, id=request.GET.get('new_song', '')))
        obj.save()
        return redirect(f'/playlist/{obj.id}')

    context = {
        'page_title': f"Playlist - {obj.name}",
        'object': obj,
        'full_duration': duration,
        'songs': Song.objects.all(),
    }

    return render(request, 'playlist/playlist_detail.html', context)

@login_required
def playlist_edit_view(request, playlist_id):
    obj = get_object_or_404(Playlist, id=playlist_id)  

    form = PlaylistForm(request.POST or None, instance=obj)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('/playlist')
    
    context = {
        'page_title': f"Edit playlist - {obj.name}",
        'form': form
    }

    return render(request, 'playlist/playlist_add.html', context)

def playlist_delete_view(request, playlist_id):
    obj = get_object_or_404(Playlist, id=playlist_id)  

    if request.method == 'POST':
        obj.delete()
        return redirect('/playlist')

    context = {
        'page_title': f"Delete playlist - {obj.name}",
        'object': obj,
    }

    return render(request, 'playlist/playlist_delete.html', context)