from django.shortcuts import render, get_object_or_404, redirect

from .models import Genre
from .forms import GenreForm

# Create your views here.
def genre_add_view(request):
    form = GenreForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('/genre')

    context = {
        'page_title': 'Add genre',
        'form': form,
    }

    return render(request, 'genre/genre_add.html', context)

def genre_list_view(request):
    queryset = Genre.objects.all()
    
    context = {
        'page_title': 'All genres',
        'object_list': queryset,
    }

    return render(request, 'genre/genre_list.html', context)

def genre_detail_view(request, genre_id):
    obj = get_object_or_404(Genre, id=genre_id)

    obj.clicks += 1
    obj.save()

    songs = obj.song_set.all()
    songs = sorted(songs, key = lambda x: x.views, reverse = True)

    context = {
        'page_title': f"Genre - {obj.name}",
        'object': obj, 
        'song_list': songs,
    }

    return render(request, 'genre/genre_detail.html', context)

def genre_edit_view(request, genre_id):
    obj = get_object_or_404(Genre, id=genre_id)  

    form = GenreForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('/genre')
    
    context = {
        'page_title': f"Edit genre - {obj.name}",
        'form': form
    }

    return render(request, 'genre/genre_add.html', context)

def genre_delete_view(request, genre_id):
    obj = get_object_or_404(Genre, id=genre_id)  

    if request.method == 'POST':
        obj.delete()
        return redirect('/genre')

    context = {
        'page_title': f"Delete genre - {obj.name}",
        'object': obj,
    }

    return render(request, 'genre/genre_delete.html', context)