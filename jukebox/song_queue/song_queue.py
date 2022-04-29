from django.shortcuts import get_object_or_404
from song.models import Song
from playlist.models import Playlist

class SongQueue():

    @staticmethod
    def addSong(request):
        song = get_object_or_404(Song, id=request.POST.get('song_id',''))

        try:
            request.session['queue'].append(song.id)
        except:
            request.session['queue'] = []
            request.session['queue_index'] = 0
            request.session['queue'].append(song.id)
            
        request.session.modified = True

    @staticmethod
    def clearQueue(request):
        request.session['queue'] = []
        request.session['queue_index'] = 0

        request.session.modified = True

    @staticmethod
    def saveAsPlaylist(song_id_list, playlist_name, user):
        new = Playlist(name = playlist_name)
        new.user = user
        new.save()

        for song_id in song_id_list:
            new.songs.add(get_object_or_404(Song, id = song_id))
        new.save()

        return new

    @staticmethod
    def removeFromQueue(request, index):
        request.session['queue'].pop(int(index))

        request.session.modified = True