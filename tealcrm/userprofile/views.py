from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from .models import Userprofile
 
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # Check if the form is valid
        if form.is_valid():
            # Save the user to the database
            user=form.save()
            # Create a userprofile object for the user
            Userprofile.objects.create(user=user)
            # Redirect to the login page
            return redirect('/login/')
    else:    
        form = UserCreationForm()
    return render(request, 'userprofile/signup.html', {'form': form})

# Path: tealcrm/userprofile/views.py