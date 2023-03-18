from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Recipe_Main"),
    path('login/', views.login, name="Recipe_Login"),
    path('register/', views.register, name="Recipe_Register"),
]