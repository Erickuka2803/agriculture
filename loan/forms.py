from django import forms
from .models import LoanApplication

class LoanApplicationForm(forms.ModelForm):
    class Meta:
        model = LoanApplication
        fields = ['name', 'income', 'farm_size', 'credit_score', 'requested_amount']
