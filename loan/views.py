from django.shortcuts import render, redirect, get_object_or_404
from .models import LoanApplication
from .forms import LoanApplicationForm
from django.shortcuts import render
from .models import Loan  # Ensure the model is imported if you're fetching data

# Home page view
def home(request):
    return render(request, 'home.html')

# About page view
def about(request):
    return render(request, 'about.html')

# Services page view
def services(request):
    return render(request, 'services.html')

# Apply for loan view
def apply_for_loan(request):
    if request.method == 'POST':
        form = LoanApplicationForm(request.POST)
        if form.is_valid():
            application = form.save()  # Save the form to the database
            return redirect('loan:loan_result', pk=application.pk)  # Redirect to loan result page with the application pk
    else:
        form = LoanApplicationForm()  # Create a blank form if not POST
    return render(request, 'loan/apply_for_loan.html', {'form': form})

def my_view(request):
    # some logic here
    return render(request, 'my_template.html', {'context': context_data})


def home(request):
    loans = Loan.objects.all()  # Retrieve loan data from the database
    return render(request, 'home.html', {'loans': loans})  # Pass data to template

# Loan result page view
def loan_result(request, pk):
    # Use get_object_or_404 to handle potential missing application gracefully
    application = get_object_or_404(LoanApplication, pk=pk)
    score = application.score()  # Assuming 'score' is a method on LoanApplication
    return render(request, 'loan/loan_result.html', {'application': application, 'score': score})
