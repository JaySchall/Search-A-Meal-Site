from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Recipe_Main"),
    path('login/', views.loginUser, name="Recipe_Login"),
    path('logout/', views.logoutUser, name="Recipe_Logout"),
    path('register/', views.register, name="Recipe_Register"),
    path('about/', views.about, name="Recipe_About"),
    path('account/', views.account, name="Recipe_Account"),
    path('<name>/', views.recipeItem, name="Recipe_Item"),
    path('<name>/save/', views.addRecipe, name="Recipe_Save"),
    path('<name>/del/', views.delRecipe, name="Recipe_Delete"),
]