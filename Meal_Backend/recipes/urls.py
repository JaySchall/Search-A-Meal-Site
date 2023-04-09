from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Recipe_Main"),
    path('login/', views.loginUser, name="Recipe_Login"),
    path('register/', views.register, name="Recipe_Register"),
    path('about/', views.about, name="Recipe_About"),
    path('<name>/', views.recipeItem, name="Recipe_Item"),
]