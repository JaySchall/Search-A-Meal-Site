from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from .forms import registerForm, loginForm
from .models import Users
# Create your views here.
def home(request):
    return render(request, 'MainMenu.html')

def login(request):
    if request.method == "POST":
        form = loginForm(request.POST)
        return render(request, 'register.html')
    else:
        form = loginForm()
        return render(request, 'login.html', {'form': form})


def register(request):
    
    if request.method == "POST":
        form = registerForm(request.POST)
        if form.is_valid():
            sign_up = form.save(commit=False)
            sign_up.password = make_password(form.cleaned_data["password"])
            sign_up.save()
            return render(request, 'login.html')
        else:
            print(form.errors)
            return render(request, 'register.html')
            
    else:
        form = registerForm()
        return render(request, 'register.html', {'form': form})
