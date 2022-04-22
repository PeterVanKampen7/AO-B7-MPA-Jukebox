from django.shortcuts import get_object_or_404
from song.models import Song

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
    def saveAsPlaylist():

        print()
