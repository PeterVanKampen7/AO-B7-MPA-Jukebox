from datetime import timedelta
from django.shortcuts import get_object_or_404, redirect, render
from song.models import Song
from song_queue.song_queue import SongQueue

# Create your views here.

def queue_detail(request):
    # Create view for the queue detail page

    # If user has pressed the next song button, run the method in the song_queue Class
    if request.POST.get('next_song',''):
        SongQueue.nextSong(request)

    # If user has pressed the previous song button, run the method in the song_queue Class
    if request.POST.get('previous_song',''):
        SongQueue.prevSong(request)

    # If user has pressed the clear queue button, run the method in the song_queue Class
    if request.POST.get('clear_queue',''):
        SongQueue.clearQueue(request)

    # If user has pressed the save queue button, run the method in the song_queue Class
    if request.POST.get('save_queue',''):
        # pass the name and current user as paramenters
        playlist = SongQueue.saveAsPlaylist(request.session['queue'], request.POST.get('new_playlist_name', ''), request.user)
        # Redirect to the Playlist that was just made
        return redirect(f'/playlist/{playlist.id}')

    # If user has pressed the delete song button, run the method in the song_queue Class
    if request.GET.get('delete_entry', ''):
        SongQueue.removeFromQueue(request, request.GET.get('delete_entry', ''))
        # Redirect to queue detail page
        return redirect('/song_queue')
        

    # These oprations will fail if no queue exists yet
    try:
        # Get the queue filled with song id's
        song_id_list = request.session['queue'] or None
        song_list = []

        # Create empty timedelta to track total duration of the queue
        queue_duration = timedelta()
    
        # Fill array with Song objects, retrieved with the song id's from the queue
        for song_id in song_id_list:
            song = get_object_or_404(Song, id=song_id)
            song_list.append(song)
            queue_duration += song.duration

        # Set a variable with the current song
        current_song_index = request.session['queue_index']
        current_song = song_list[current_song_index]  
    except:
        # If no queue exists redirect to Home page
        return redirect('/')

    # Pass page name, queue, queue duration, current song and current song index into context
    context = {
        'page_title': 'Song queue',
        'queue': song_list,
        'queue_duration': queue_duration,
        'current_song': current_song,
        'current_song_index': current_song_index,
    }

    # Render the template
    return render(request, 'song_queue/queue_detail.html', context)