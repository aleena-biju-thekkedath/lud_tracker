from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","email","password","password2"]

        widgets = {
            "username": forms.TextInput(attrs= {"class": "form-control","placeholder":"UserName"}),
            "email": forms.TextInput(attrs= {"class": "form-control","placeholder":"Email Id"}),
            "password" : forms.PasswordInput(attrs= {"class": "form-control","placeholder":"Password"}),
            "password2": forms.PasswordInput(attrs= {"class": "form-control","placeholder":"Confirm Password"}),
        }