from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import Users
from . import models

class registerForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ("email", "password")
        
class loginForm(AuthenticationForm):
    class Meta:
        model = Users
        fields = ("email", "password")
        