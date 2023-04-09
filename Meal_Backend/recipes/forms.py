from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms
from .models import Users
from . import models

class registerForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ("email", "password")
        
#class loginForm(AuthenticationForm):
 #   class Meta:
 #       model = Users
 #      fields = ("email", "password")

class loginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput(render_value = True))