from django.shortcuts import render
from requests import request

# Create your views here.

def home(request):
    
    return render(request, 'index.html')

