from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import registerForm, loginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Users, Recipe
# Create your views here.
def home(request):
    recipes = Recipe.objects.all()
    
    query = request.GET.get('q')
    if query:
        recipes = Recipe.objects.filter(name__icontains=query)
    context = {
        "recipes": recipes,
    }
    return render(request, 'MainMenu.html', context)

#def search(request):
    #allrecipes = Recipe.objects.all()

def login(request):
    if request.method == "POST":
        #form = loginForm(data=request.POST)
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(email=form.cleaned_data["email"], password=form.cleaned_data["password"])
            if user is not None:
                login(request, user)
                return redirect("/recipes")
            else:
                messages.error(request,"Invalid username or password.")
                print("huh")
        else:
            messages.error(request,"Invalid username or password.")
            print(form.errors)
    form = loginForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    
    if request.method == "POST":
        form = registerForm(request.POST)
        if form.is_valid():
            user = Users.objects.create_user(form.cleaned_data["email"], form.cleaned_data["password"])
            return redirect("../login")
        else:
            print(form.errors)
            return render(request, 'register.html')
            
    else:
        form = registerForm()
        return render(request, 'register.html', {'form': form})
