from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import make_password
from .forms import registerForm, loginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Users, Recipe, Link
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

def loginUser(request):
    if request.method == "POST":
        form = loginForm(request.POST)
        #form = AuthenticationForm(request, data=request.POST)
        print("ok1")
        if form.is_valid():
            print(make_password(form.cleaned_data["password"]))
            user = authenticate(request, email=form.cleaned_data["email"], password=form.cleaned_data["password"])
            if user is not None:
                login(request, user)
                return redirect("/recipes/account")
            else:
                messages.error(request,"Invalid username or password.")
                print("huh")
        else:
            messages.error(request,"Invalid username or password.")
            print(form.errors)
    form = loginForm()
    return render(request, 'login.html', {'form': form})
def logoutUser(request):
    logout(request)
    return redirect("/")

def register(request):
    
    if request.method == "POST":
        form = registerForm(request.POST)
        if form.is_valid():
            print(make_password(form.cleaned_data["password"]))
            user = Users.objects.create_user(form.cleaned_data["email"], form.cleaned_data["password"])
            return redirect("../login")
        else:
            print(form.errors)
            return render(request, 'register.html')
            
    else:
        form = registerForm()
        return render(request, 'register.html', {'form': form})

def about(request):
    return render(request, 'AboutPage.html')

def account(request):
    
    if request.user.is_authenticated:
        linked = Link.objects.filter(email=request.user.id)
        print(linked)
        recipes = []
        for id in linked:
            print(id)
            recipes.append(Recipe.objects.get(id=id.id.id))
        context = {
        "recipes": recipes,
    }
        return render(request, 'UserPage.html', context)
    else:
        return redirect("../login")

def recipeItem(request, name):
    recipe = Recipe.objects.get(name=name)
    link = Link.objects.filter(id=recipe.id, email=request.user.id)
    print(link)
    context = {
        'recipe': recipe,
        'link': link,
    }
    return render(request, 'recipe.html', context)

def addRecipe(request, name):
    recipe = Recipe.objects.get(name=name)
    if request.user.is_authenticated:
        try:
            existing = Link.objects.get(id=recipe, email=request.user)
            print(existing)
        except:
            
            print(request.user.email +" " + str(recipe.id))
            linked = Link.objects.create(id=recipe, email=request.user)
            return redirect("../")

        print("exists already")
        return redirect("../")
    else:
        return redirect("../")
def delRecipe(request, name):
    recipe = Recipe.objects.get(name=name)
    if request.user.is_authenticated:
        try:
            existing = Link.objects.get(id=recipe, email=request.user)
            existing.delete()
            return redirect("../")
        except:
            print("Can't remove what isn't real")
            return redirect("../")
    else:
        return redirect("../")