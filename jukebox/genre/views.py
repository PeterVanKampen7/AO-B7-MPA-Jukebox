from django.shortcuts import render, get_object_or_404, redirect

from .models import Genre
from .forms import GenreForm

# Create your views here.
def genre_add_view(request):
    # Create view for adding a genre

    # Instantiate the form, if data for the form exists in POST or aomg FILES pass them along
    form = GenreForm(request.POST or None, request.FILES or None)

    # If form is valid, save new genre into DB and redirect to genre list
    if form.is_valid():
        form.save()
        return redirect('/genre')

    # Add page name and form into context
    context = {
        'page_title': 'Add genre',
        'form': form,
    }

    # Render the template
    return render(request, 'genre/genre_add.html', context)

def genre_list_view(request):
    # Create view for listing all genres

    # Get all genres
    queryset = Genre.objects.all()
    
    # Enter page name and all genres into context
    context = {
        'page_title': 'All genres',
        'object_list': queryset,
    }

    # Render the template
    return render(request, 'genre/genre_list.html', context)

def genre_detail_view(request, genre_id):
    # Create view for genre detail view

    # get genre with id passed int the URL through the route
    obj = get_object_or_404(Genre, id=genre_id)

    # Up the amount of clicks for this genre by 1 and save into DB
    obj.clicks += 1
    obj.save()

    # Get all songs associated with this genre and sort them DESC on clicks
    songs = obj.song_set.all()
    songs = sorted(songs, key = lambda x: x.views, reverse = True)

    # Pass page name, Genre and Songs into context
    context = {
        'page_title': f"Genre - {obj.name}",
        'object': obj, 
        'song_list': songs,
    }

    # render the template
    return render(request, 'genre/genre_detail.html', context)

def genre_edit_view(request, genre_id):
    # Create view for editing a genre

    # Get the genre with the id in the URL passd through the route
    obj = get_object_or_404(Genre, id=genre_id)  

    # Instantiate the form, if data for the form exists in POST or aomg FILES pass them along
    form = GenreForm(request.POST or None, request.FILES or None, instance=obj)

    # If the form is valid, save the changes and redirect to genre list
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('/genre')
    
    # Pass page name and form into context
    context = {
        'page_title': f"Edit genre - {obj.name}",
        'form': form
    }

    # Render the template
    return render(request, 'genre/genre_add.html', context)

def genre_delete_view(request, genre_id):
    # Create view to delete genre

    # Get genre with the id passed in the url through the route
    obj = get_object_or_404(Genre, id=genre_id)  

    # If delete form is submitted delete the genre and redirect to genre list
    if request.method == 'POST':
        obj.delete()
        return redirect('/genre')

    # Pass page name and Genre into context
    context = {
        'page_title': f"Delete genre - {obj.name}",
        'object': obj,
    }

    # Render the template
    return render(request, 'genre/genre_delete.html', context)