from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArtistForm
from .models import Artist

# Create your views here.
def artist_add_view(request):
    form = ArtistForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/artist')

    context = {
        'page_title': 'Add artist',
        'form': form,
    }

    return render(request, 'artist/artist_add.html', context)

def artist_list_view(request):
    queryset = Artist.objects.all()

    context = {
        'page_title': 'All artists',
        'object_list': queryset,
    }

    return render(request, 'artist/artist_list.html', context)

def artist_detail_view(request, artist_id):
    obj = get_object_or_404(Artist, id=artist_id)

    context = {
        'page_title': f'Artist - {obj.name}',
        'object': obj,
    }

    return render(request, 'artist/artist_detail.html', context)

def artist_edit_view(request, artist_id):
    obj = get_object_or_404(Artist, id=artist_id)  

    form = ArtistForm(request.POST or None, instance=obj)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('/artist')
    
    context = {
        'page_title': f"Edit artist - {obj.name}",
        'form': form
    }

    return render(request, 'artist/artist_add.html', context)

def artist_delete_view(request, artist_id):
    obj = get_object_or_404(Artist, id=artist_id)  

    if request.method == 'POST':
        obj.delete()
        return redirect('/artist')

    context = {
        'page_title': f"Delete artist - {obj.name}",
        'object': obj,
    }

    return render(request, 'artist/artist_delete.html', context)