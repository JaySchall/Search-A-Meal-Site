from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'MainMenu.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')