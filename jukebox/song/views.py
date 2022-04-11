from django.shortcuts import get_object_or_404, redirect, render
from .models import Song
from .forms import SongForm

# Create your views here.
def song_add_view(request):
    form = SongForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('/song')

    context = {
        'page_title': 'Add song',
        'form': form,
    }

    return render(request, 'song/song_add.html', context)

def song_list_view(request):
    querylist = Song.objects.all()

    context = {
        'page_title': 'All songs',
        'object_list': querylist,
    }

    return render(request, 'song/song_list.html', context)

def song_detail_view(request, song_id):
    obj = get_object_or_404(Song, id=song_id)

    context = {
        'page_title': f'Song - {obj.name}',
        'object': obj,
    }

    return render(request, 'song/song_detail.html', context)

def song_edit_view(request, song_id):
    obj = Song.objects.get(id=song_id)

    form = SongForm(request.POST or None, request.FILES or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect('/song')

    context = {
        'page_title': f'Edit song - {obj.name}',
        'form': form,
    }

    return render(request, 'song/song_add.html', context)