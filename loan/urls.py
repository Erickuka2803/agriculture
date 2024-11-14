from django.conf import settings
from django.shortcuts import render, get_object_or_404
from . import views
from django.urls import path


# View to render loan result page based on primary key (pk)
def loan_result(request, pk):
    loan = get_object_or_404(Loan, pk=pk)  # Get the loan object by primary key
    return render(request, 'loan_result.html', {'loan': loan})

# Other views (ensure these are defined if not already)
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def apply_for_loan(request):
    return render(request, 'apply_for_loan.html')

app_name = 'loan'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('apply/', views.apply_for_loan, name='apply_for_loan'),
    path('result/<int:pk>/', views.loan_result, name='loan_result'),
]