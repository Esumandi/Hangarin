from django.shortcuts import render
from django.views.generic import ListView
#from .models import

# Create your views here.

def home(request):
    """Render the application homepage."""
    return render(request, 'home.html')
