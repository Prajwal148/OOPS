# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile

@login_required
def profile_view(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user  # Ensure the profile is associated with the logged-in user
            profile.save()
            return redirect('userprofile')  # Redirect to the profile page after saving
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profile.html', {'form': form})

@login_required
def userprofile(request):
    # Try to get the profile for the logged-in user, or create one if it doesn't exist
    profile, created = Profile.objects.get_or_create(user=request.user)

    # Initialize the form with the user's profile instance
    form = ProfileForm(request.POST or None, instance=profile)

    if form.is_valid():
        form.save()  # Save the profile data
        return redirect('userprofile')  # Redirect to avoid re-posting the form on refresh

    return render(request, 'userprofile.html', {'form': form, 'profile': profile})
