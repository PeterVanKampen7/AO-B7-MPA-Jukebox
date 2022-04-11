"""jukebox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from home.views import home_view
from genre.views import (
    genre_add_view, 
    genre_list_view, 
    genre_detail_view, 
    genre_edit_view, 
    genre_delete_view,
)
from artist.views import (
    artist_add_view,
    artist_list_view,
    artist_detail_view,
    artist_edit_view,
    artist_delete_view,
)

urlpatterns = [
    path('', home_view, name='home'),

    path('genre/', genre_list_view, name='genre_list'),
    path('genre/<int:genre_id>/', genre_detail_view, name='genre_detail'),
    path('genre/<int:genre_id>/edit/', genre_edit_view, name='genre_edit'),
    path('genre/<int:genre_id>/delete/', genre_delete_view, name='genre_delete'),
    path('genre/new/', genre_add_view, name='genre_add'),

    path('artist/', artist_list_view, name='artist_list'),
    path('artist/<int:artist_id>/', artist_detail_view, name='artist_detail'),
    path('artist/<int:artist_id>/edit/', artist_edit_view, name='artist_edit'),
    path('artist/<int:artist_id>/delete/', artist_delete_view, name='artist_delete'),
    path('artist/new/', artist_add_view, name='artist_add'),
    

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)