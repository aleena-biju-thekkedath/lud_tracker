from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","email"]

        widgets = {
            "username": forms.TextInput(attrs= {"class": "form-control","placeholder":"UserName"}),
            "email": forms.TextInput(attrs= {"class": "form-control","placeholder":"Email Id"}),
            }