from django.shortcuts import get_object_or_404
from song.models import Song
from playlist.models import Playlist

class SongQueue():
    # This class handles all interaction with the SESSION
    # (SESSION in Django is in fact a COOKIE)

    @staticmethod
    # This method is static and adds a song to the queue
    def addSong(request):
        # Get the song with the id passed through the submitted form
        song = get_object_or_404(Song, id=request.POST.get('song_id',''))

        # Try to add the song into the queue
        try:
            request.session['queue'].append(song.id)
        # If this fails the queue does not exist yet
        # Make the queue first and then add the song to it
        except:
            request.session['queue'] = []
            # This index tracks what song in the queue is currently being 'played'
            request.session['queue_index'] = 0
            request.session['queue'].append(song.id)
            
        # Indicate to Django the Session has been modified so that the changes will be saved
        request.session.modified = True

    @staticmethod
    # This method is static and moves the queue to the next song
    def nextSong(request):
        # If the current index is not already at the last song moves the index up by one
        if len(request.session['queue']) - 1 > request.session['queue_index']:
            request.session['queue_index'] += 1

            # Indicate to Django the Session has been modified so that the changes will be saved
            request.session.modified = True

    @staticmethod
    # This method is static and moves the queue to the previous song
    def prevSong(request):
        # If the queue is not already at the first song decrease the index by one
        if 0 < request.session['queue_index']:
            request.session['queue_index'] -= 1

            # Indicate to Django the Session has been modified so that the changes will be saved
            request.session.modified = True

    @staticmethod
    # This method is static and clears the entire queue
    def clearQueue(request):
        # Create a new empty queue and set the index to 0
        request.session['queue'] = []
        request.session['queue_index'] = 0

        # Indicate to Django the Session has been modified so that the changes will be saved
        request.session.modified = True

    @staticmethod
    # This method is static and saves the queue as a Playlist
    def saveAsPlaylist(song_id_list, playlist_name, user):
        # Create a new playlist with the name passed as parameter
        new = Playlist(name = playlist_name)
        # Add the current user as owner of this new Playlist
        new.user = user
        # Save the new playlist. Without saving the foreign key relations cannot be added
        new.save()

        # For each song in the queue add it to the new Playlist
        for song_id in song_id_list:
            new.songs.add(get_object_or_404(Song, id = song_id))

        # Save the Playlist
        new.save()

        # Return the Playlist
        return new

    @staticmethod
    # This method removes a song from the queueu, indicated by an index
    def removeFromQueue(request, index):
        # Remove the song from the queue at the index passed as parameter
        request.session['queue'].pop(int(index))

        # Indicate to Django the Session has been modified so that the changes will be saved
        request.session.modified = True