from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArtistForm
from .models import Artist

# Create your views here.

def artist_add_view(request):
    # Create the view for adding an artist

    # Instantiate the form, if data for the form exists in POST or aomg FILES pass them along
    form = ArtistForm(request.POST or None, request.FILES or None)

    # If the submitted form is valid save into the database and redirect user to artist list
    if form.is_valid():
        form.save()
        return redirect('/artist')

    # Pass page name and form into context, to be used in the template
    context = {
        'page_title': 'Add artist',
        'form': form,
    }

    # Render the template
    return render(request, 'artist/artist_add.html', context)

def artist_list_view(request):
    # Create the view for listing all artists

    # Get all existing Artists out of the database
    queryset = Artist.objects.all()

    # Pass the page name and all artist into context, to be used in the template
    context = {
        'page_title': 'All artists',
        'object_list': queryset,
    }

    # Render the template
    return render(request, 'artist/artist_list.html', context)

def artist_detail_view(request, artist_id):
    # Create the view for a single artist detail view

    # Get the artist with the id passed in the url through the route
    obj = get_object_or_404(Artist, id=artist_id)

    # Increase the amount of times this artist has been viewed and save this
    obj.clicks += 1
    obj.save()

    # Get all songs related to this artist
    songs = obj.song_set.all()
    # Sort songs on views DESC
    songs = sorted(songs, key = lambda x: x.views, reverse = True)

    # Pass page name, Artist and Songs into context, to be used in the template
    context = {
        'page_title': f'Artist - {obj.name}',
        'object': obj,
        'song_list': songs,
    }

    # Render the template
    return render(request, 'artist/artist_detail.html', context)

def artist_edit_view(request, artist_id):
    # Create view for editing an artist

    # Get artist with the id passed in the URL through the route
    obj = get_object_or_404(Artist, id=artist_id)  

    # Instantiate the form, if data for the form exists in POST or aomg FILES pass them along
    form = ArtistForm(request.POST or None, request.FILES or None, instance=obj)

    # If the form is valid, save changes into the Database and redirect user to artist list
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('/artist')
    
    # Pass name and form into context, to be used in the template
    context = {
        'page_title': f"Edit artist - {obj.name}",
        'form': form
    }

    # Render the template
    return render(request, 'artist/artist_add.html', context)

def artist_delete_view(request, artist_id):
    # Create view to delete artist

    # Get artist with id passed in the URL through the route
    obj = get_object_or_404(Artist, id=artist_id)  

    # If delete form is submitted delete object and redirect to artist list 
    if request.method == 'POST':
        obj.delete()
        return redirect('/artist')

    # Pass page name and artist into context
    context = {
        'page_title': f"Delete artist - {obj.name}",
        'object': obj,
    }

    # Render the template
    return render(request, 'artist/artist_delete.html', context)