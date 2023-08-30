from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

        widgets = { 
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "User Name"}),
            "email": forms.TextInput(attrs={"class": "form-control", "placeholder": "Email Id"})

        }
        
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your password'})

        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None 





