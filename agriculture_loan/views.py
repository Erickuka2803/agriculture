from .models import Loan

def get_all_loans():
    return Loan.objects.all()

from django.shortcuts import render
from .services import get_all_loans

def apply_for_loan(request):
    # Your logic to handle loan application
    return render(request, 'apply_for_loan.html')

def loan(request):
     loans = Loan.objects.all()
     return render(request, 'loan.html', {'loans': loans})

from django.apps import apps
from django.template.loader import get_template
from django.http import HttpResponse
from .views import loan
from .services import get_all_loans


# Create your views here.
def home(request):
    return render(request, 'home.html')  # Render the home page template
    print(get_template('home.html'))
    return HttpResponse("Check the server logs for template search directories.")

def loan(request):
    Loan = apps.get_model('agriculture_loan', 'Loan')     # Move the import inside the function to avoid circular import

def loan(request):
    from agriculture_loan.models import Loan 
    # Function code here
    pass

