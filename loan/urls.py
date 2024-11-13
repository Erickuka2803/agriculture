from django.urls import path
from . import views

app_name = 'loan'

urlpatterns = [
    path('apply/', views.apply_for_loan, name='apply_for_loan'),
    path('result/<int:pk>/', views.loan_result, name='loan_result'),
]
