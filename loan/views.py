from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import LoanApplication
from .forms import LoanApplicationForm

def apply_for_loan(request):
    if request.method == 'POST':
        form = LoanApplicationForm(request.POST)
        if form.is_valid():
            application = form.save()
            return redirect('loan:loan_result', pk=application.pk)
    else:
        form = LoanApplicationForm()
    return render(request, 'loan/apply_for_loan.html', {'form': form})

def loan_result(request, pk):
    application = LoanApplication.objects.get(pk=pk)
    score = application.score()
    return render(request, 'loan/loan_result.html', {'application': application, 'score': score})

