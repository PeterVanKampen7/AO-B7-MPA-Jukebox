from django.shortcuts import get_object_or_404, redirect, render
from song.models import Song
from song_queue.song_queue import SongQueue

# Create your views here.
def queue_detail(request):
    if request.POST.get('next_song',''):
        SongQueue.nextSong(request)

    if request.POST.get('previous_song',''):
        SongQueue.prevSong(request)

    if request.POST.get('clear_queue',''):
        SongQueue.clearQueue(request)

    if request.POST.get('save_queue',''):
        playlist = SongQueue.saveAsPlaylist(request.session['queue'], request.POST.get('new_playlist_name', ''), request.user)
        return redirect(f'/playlist/{playlist.id}')

    if request.GET.get('delete_entry', ''):
        SongQueue.removeFromQueue(request, request.GET.get('delete_entry', ''))
        return redirect('/song_queue')
        

    try:
        song_id_list = request.session['queue'] or None
        song_list = []
    
        for song_id in song_id_list:
            song_list.append(get_object_or_404(Song, id=song_id))

        current_song_index = request.session['queue_index']
        current_song = song_list[current_song_index]  
    except:
        return redirect('/')

    context = {
        'page_title': 'Song queue',
        'queue': song_list,
        'current_song': current_song,
        'current_song_index': current_song_index,
    }

    return render(request, 'song_queue/queue_detail.html', context)