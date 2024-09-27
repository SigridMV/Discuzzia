from django.shortcuts import render, redirect  
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth import login  # Import the login function to authenticate users
from django.contrib.auth.decorators import login_required  # Import the login_required decorator to restrict access

def signup(request):
    """
    Handles user signup functionality.
    If the request method is POST, it processes the submitted form.
    If the form is valid, it creates a new user and logs them in.
    Otherwise, it renders an empty signup form.
    """
    # Check if the request method is POST
    if request.method == 'POST':  
        form = UserCreationForm(request.POST)  # Instantiate the form with submitted data
        if form.is_valid():  # Check if the form is valid
            user = form.save()  # Save the new user to the database
            login(request, user)  # Log the user in
            return redirect('index')  # Redirect to the main page
    else:
        form = UserCreationForm()  # Instantiate an empty form for GET requests
    return render(request, 'accounts/signup.html', {'form': form})  # Render the signup template with the form

@login_required
def profile(request):
    """
    Renders the user profile page.
    This view is restricted to authenticated users only.
    """
    return render(request, 'accounts/profile.html')  # Render the profile template for the user

 






