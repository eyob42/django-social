from django.shortcuts import render, redirect
from .forms import DweetForm
from .models import Profile

def dashboard(request):
    # IF THE USER IS SUBMITTING A FORM (Clicking the "Dweet" button)
    if request.method == "POST":
        form = DweetForm(request.POST) # Fill the form with the text the user typed
        if form.is_valid(): # Check if the message is okay (e.g., not empty)
            dweet = form.save(commit=False) # "Prepare to save the dweet, but wait a moment!"
            dweet.user = request.user # Write YOUR username onto the dweet
            dweet.save() # NOW save it to the database
            return redirect("dwitter:dashboard") #Stop the Double-Posts with a "Redirect"
    # FOR BOTH 'POST' AND NORMAL PAGE LOADS, do this:
    form = DweetForm() # Show a fresh, empty form
    return render(request, "dwitter/dashboard.html", {"form": form})


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "dwitter/profile_list.html",{"profiles":profiles})


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
    return render(request, "dwitter/profile.html",{"profile":profile})