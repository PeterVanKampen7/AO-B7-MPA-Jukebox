from django.shortcuts import render, get_object_or_404

from .models import Genre

# Create your views here.
def genre_add_view(request):
    context = {
        'page_title': 'Add genre',
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

    context = {
        'page_title': obj.name,
    }

    return render(request, 'genre/genre_detail.html', context)