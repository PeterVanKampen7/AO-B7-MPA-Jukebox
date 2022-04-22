from django.shortcuts import get_object_or_404, render, get_list_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Playlist
from .forms import PlaylistForm

# Create your views here.
@login_required
def playlist_add_view(request):
    form = PlaylistForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/playlist')

    context = {
        'page_title': 'Add playlist',
        'form': form,
    }

    return render(request, 'playlist/playlist_add.html', context)

def playlist_list_view(request):
    queryset = Playlist.objects.all()

    context = {
        'page_title': 'All playlists',
        'object_list': queryset,
    }

    return render(request, 'playlist/playlist_list.html', context)

def playlist_detail_view(request, playlist_id):
    obj = get_object_or_404(Playlist, id=playlist_id)

    context = {
        'page_title': f"Playlist - {obj.name}",
        'object': obj,
    }

    return render(request, 'playlist/playlist_detail.html', context)

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