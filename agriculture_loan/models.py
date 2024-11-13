# agriculture_loan/models.py
from django.db import models

# Define your models here (example)
class Loan(models.Model):
    # Example fields
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
