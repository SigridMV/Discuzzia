from django.shortcuts import render, redirect  
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth import login  # Import the login function to authenticate users
from django.contrib.auth.decorators import login_required  # Import the login_required decorator to restrict access
from .forms import CustomUserChangeForm
from django.contrib import messages
from django.contrib.auth import logout

def signup(request):
    """
    Handles user signup functionality.
    If the request method is POST, it processes the submitted form.
    If the form is valid, it creates a new user and logs them in.
    Otherwise, it renders an empty signup form.
    """
    if request.method == 'POST':  
        form = UserCreationForm(request.POST)  
        if form.is_valid():  
            user = form.save()  
            login(request, user)  
            return redirect('index')  
    else:
        form = UserCreationForm()  
    return render(request, 'accounts/signup.html', {'form': form})  

@login_required
def profile(request):
    """
    Allows users to view and edit their profile.
    Handles both GET requests to display the form and POST requests to update the profile.
    """
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)  # Usar el formulario personalizado
        if form.is_valid():
            form.save()  # Guarda los cambios
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=request.user)  # Prellenar con los datos actuales

    # Pasar la información adicional del último login y la URL de restablecimiento de contraseña
    context = {
        'form': form,
        'last_login': request.user.last_login,
    }

    return render(request, 'accounts/profile.html', context) 

def custom_logout(request):
    logout(request) 
    return redirect('index')
 






