from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
def home_view(request, *args, **kwargs):

    context = {
        'page_title': 'Home',
    }

    return render(request, 'home.html', context)

def user_profile_view(request):

    context = {
        'page_title': f'User - {request.user}',
    }

    return render(request, 'registration/profile.html', context)

def user_registration_view(request):

    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(request, user)
        return redirect('home')

    context = {
        'form': form,
    }

    return render(request, 'registration/registration.html', context)