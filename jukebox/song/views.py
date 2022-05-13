from django.shortcuts import get_object_or_404, redirect, render

from song_queue.song_queue import SongQueue
from .models import Song
from .forms import SongForm

# Create your views here.
def song_add_view(request):
    # Create view for adding new songs

    # Instantiate the form, if data for the form exists in POST or among FILES pass them along
    form = SongForm(request.POST or None, request.FILES or None)

    # If the submitted form is valid save the song and reidrect to song list page
    if form.is_valid():
        form.save()
        return redirect('/song')

    # Pass page name and form into context
    context = {
        'page_title': 'Add song',
        'form': form,
    }

    # Render the template
    return render(request, 'song/song_add.html', context)

def song_list_view(request):
    # Create view to list all songs

    # Get all songs
    querylist = Song.objects.all()

    # Pass page name and all songs into context
    context = {
        'page_title': 'All songs',
        'object_list': querylist,
    }

    # Render the template
    return render(request, 'song/song_list.html', context)

def song_detail_view(request, song_id):
    # Create view for song detail page
    
    # This functin checks if the user has pressed the button to add this song to the queue
    add_song_to_queue(request)

    # Get the song with the id in the URL passed through the route
    obj = get_object_or_404(Song, id=song_id)
    
    # Up the views for this song by 1 and save
    obj.views += 1
    obj.save()

    # Pass page name and Song into context
    context = {
        'page_title': f'Song - {obj.name}',
        'object': obj,
    }

    # Render the template
    return render(request, 'song/song_detail.html', context)

def song_edit_view(request, song_id):
    # Create the view to edit a Song

    # Get the song with the id in the URL passed through the route
    obj = get_object_or_404(Song, id=song_id)

    # Instantiate the form, if data for the form exists in POST or aomg FILES pass them along. 
    # Add current object to form to fill in existing data
    form = SongForm(request.POST or None, request.FILES or None, instance=obj)

    # If the submitted form is valid save the changes and redirect to song list page
    if form.is_valid():
        form.save()
        return redirect('/song')

    # Pass page name and form into context
    context = {
        'page_title': f'Edit song - {obj.name}',
        'form': form,
    }

    # Render the template
    return render(request, 'song/song_add.html', context)

def song_delete_view(request, song_id):
    # Create the view to delete a Song

    # Get the song with the id from the URL passed through the route
    obj = get_object_or_404(Song, id=song_id)

    # If the delete form is submitted delete the song and redirect to song list page
    if request.method == 'POST':
        obj.delete()
        return redirect('/song')

    # Pass page name and Song into context
    context = {
        'page_title': f"Delete song - {obj.name}",
        'object': obj,
    }

    # Render the template
    return render(request, 'song/song_delete.html', context)

# Function to check if song has to be added to queue
def add_song_to_queue(request):
    # If button is pressed run function that adds this song to the queue
    if request.POST.get('addToQueue', ''):
        SongQueue.addSong(request)   
