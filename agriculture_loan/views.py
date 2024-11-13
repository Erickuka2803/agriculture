from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')  # Render the home page template
    print(get_template('home.html'))
    return HttpResponse("Check the server logs for template search directories.")
