from django import forms
from .models import Users
from . import models

class registerForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ("email", "displayname", "password")
        
class loginForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ("email", "password")
        