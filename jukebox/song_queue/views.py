from django.shortcuts import get_object_or_404, redirect, render
from song.models import Song
from song_queue.song_queue import SongQueue

# Create your views here.
def queue_detail(request):
    if request.POST.get('next_song',''):
        if len(request.session['queue']) - 1 > request.session['queue_index']:
            request.session['queue_index'] += 1

    if request.POST.get('clear_queue',''):
        SongQueue.clearQueue(request)

    if request.POST.get('save_queue',''):
        print('save')

    song_id_list = request.session['queue'] or None
    song_list = []

    if song_id_list is not None:
        for song_id in song_id_list:
            song_list.append(get_object_or_404(Song, id=song_id))

        current_song_index = request.session['queue_index']
        current_song = song_list[current_song_index]
    else:
        return redirect('/')

    context = {
        'page_title': 'Song queue',
        'queue': song_list,
        'current_song': current_song,
        'current_song_index': current_song_index,
    }

    return render(request, 'song_queue/queue_detail.html', context)