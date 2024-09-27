"""
URL configuration for discuzzia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include

# Define URL patterns for the entire project
urlpatterns = [
    # URL for accessing the Django admin site
    path('admin/', admin.site.urls),  
    # Include URL patterns from the 'forum' app for the root URL
    path('', include('forum.urls')),  
    # Include URL patterns from the 'accounts' app for the 'accounts/' URL
    path('accounts/', include('accounts.urls')),  
    # Include URL patterns from the 'forum' app for the 'forum/' URL
    path('forum/', include('forum.urls')),  
]
