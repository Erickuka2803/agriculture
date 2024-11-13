"""
URL configuration for agriculture_loan project.

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
from django.urls import path
from .views import apply_for_loan
from .views import loan 
from django.urls import path, include
from . import views
from agriculture_loan.views import loan


urlpatterns = [
    path('admin/', admin.site.urls),
    path('loan/', include('loan.urls')),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('loan/', loan, name='loan'),
    path('loan/', views.loan, name='loan'),
    path('apply/', views.apply_for_loan, name='apply_for_loan'),
    path('apply/', apply_for_loan, name='apply_for_loan'),
]
