from django.urls import path
from django.contrib.auth import views as auth_views 
from . import views # Import views from the current app

urlpatterns = [
     # URL for user login, rendering the specified template
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # URL for user logout, redirecting to the home page after logging out
    path('logout/', views.custom_logout, name='logout'),
     # URL for user signup, calling the signup view function
    path('signup/', views.signup, name='signup'),
     # URL for user profile, calling the profile view function
    path('profile/', views.profile, name='profile'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
]
