from django.db import models

# Create your models here.
class LoanApplication(models.Model):
    name = models.CharField(max_length=100)
    income = models.DecimalField(max_digits=10, decimal_places=2)  # Annual income
    farm_size = models.DecimalField(max_digits=10, decimal_places=2)  # Size of farm in acres
    credit_score = models.IntegerField()  # Credit score (e.g., 300 - 850)
    requested_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Loan amount requested

    def __str__(self):
        return self.name

class Loan(models.Model):
    # Define the fields for the Loan model
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    # Add other fields as necessary

    def __str__(self):
        return f"Loan for {self.loan_amount} at {self.interest_rate}%"
    
    def score(self):
        # Scoring logic based on criteria
        score = 0

        # Example scoring logic based on income
        if self.income >= 50000:
            score += 2
        elif self.income >= 20000:
            score += 1

        # Example scoring logic based on farm size
        if self.farm_size >= 100:
            score += 3
        elif self.farm_size >= 50:
            score += 2

        # Example scoring logic based on credit score
        if self.credit_score >= 700:
            score += 5
        elif self.credit_score >= 600:
            score += 3
        elif self.credit_score >= 500:
            score += 1

        # Example scoring logic based on requested loan amount
        if self.requested_amount <= 10000:
            score += 2
        elif self.requested_amount <= 50000:
            score += 1

        return score