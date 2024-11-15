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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from . import views
from agriculture_loan.views import loan  # Use only one source for the loan view
from .views import apply_for_loan  # Use only one source for apply_for_loan view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('loan.urls')),  # Adjust if your home view is in the 'loan' app
    path('', RedirectView.as_view(url='home/', permanent=False)),  # Redirect root URL to /home/
    path('', include('loan.urls')),
    path('loan/', loan, name='loan'),  # Keep only this line for the loan path
    path('apply/', apply_for_loan, name='apply_for_loan'),  # Keep only this line for the apply path
    path('about/', views.about, name='about'),
    path('home/', views.home, name='home'),
    path('services/', views.services_view, name='services'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)