from django.shortcuts import render
from .models import Loan
from .services import get_all_loans  # Keep import here

# Function to get all loans
def get_all_loans():
    return Loan.objects.all()

def home(request):
    return render(request, 'home.html')  # Make sure 'home.html' exists in your templates folder

# View to render services page
def services_view(request):
    return render(request, 'services.html')

# View to apply for loan
def apply_for_loan(request):
    # Your logic to handle loan application
    return render(request, 'apply_for_loan.html')

# View to show all loans
def loan(request):
    loans = Loan.objects.all()
    return render(request, 'loan.html', {'loans': loans})

# Base view, renders the base template
def base(request):
    return render(request, 'agriculture_loan/base.html')

# Home view, renders the home template
def home(request):
    return render(request, 'agriculture_loan/home.html')

# About view, renders the about template
def about(request):
    return render(request, 'agriculture_loan/about.html')

# Services view, renders the services template
def services(request):
    return render(request, 'agriculture_loan/services.html')
