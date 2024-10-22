from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile

# Home page
def home(request):
    return render(request, 'home.html')

# User registration
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# Profile form
@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile', user_id=request.user.id)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile/profile.html', {'form': form})

# Profile view (business card)
def profile_view(request, user_id):
    profile = Profile.objects.get(user__id=user_id)
    return render(request, 'profile/business_card.html', {'profile': profile})


