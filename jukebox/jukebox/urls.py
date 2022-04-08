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

from home.views import home_view
from genre.views import genre_add_view, genre_list_view, genre_detail_view

urlpatterns = [
    path('', home_view, name='home'),

    path('genre/', genre_list_view, name='genre_list'),
    path('genre/<int:genre_id>/', genre_detail_view, name='genre_detail'),
    path('genre/new/', genre_add_view, name='genre_add'),

    path('admin/', admin.site.urls),
]
