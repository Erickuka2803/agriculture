# project/urls.py (replace "project" with your actual project name)

from django.contrib import admin
from django.urls import path, include
from django.urls import path
from . import views  # Import your views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('agriculture_loan.urls')),  # Include URLs from the "core" app
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
]
