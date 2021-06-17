from django.shortcuts import render

# Create your views here.
from .models import Produto

def index(request):
    return render(request, 'precos\index.html')