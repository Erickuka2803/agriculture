# agriculture_loan/services.py
from .models import Loan

def get_all_loans():
    return Loan.objects.all()
