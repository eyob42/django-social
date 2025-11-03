from django.shortcuts import render, redirect
from .forms import DweetForm
from .models import Profile, Dweet

def dashboard(request):
    # Create the form ONE TIME. It's either filled with POST data or it's empty.
    form = DweetForm(request.POST or None)
    
    # Get followed dweets for both GET and POST requests
    followed_dweets = Dweet.objects.filter(
        user__profile__in=request.user.profile.follows.all()
    ).order_by("-created_at")

    # Only try to save if it's a POST request AND the data is valid
    if request.method == "POST":
        if form.is_valid():  # Check if the dweet is the right length
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            return redirect("dwitter:dashboard")  # Redirect after success

    # Render the page with the SAME form we started with.
    # If validation failed, this form contains the user's text and the error message.
    return render(
        request,
        "dwitter/dashboard.html", 
        {"form": form, "dweets": followed_dweets}
    )

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "dwitter/profile_list.html", {"profiles": profiles})

def profile(request, pk):
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()
    
    profile = Profile.objects.get(pk=pk)
    
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            # Remove the target profile from the current user's follow list
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    
    return render(request, "dwitter/profile.html", {"profile": profile})