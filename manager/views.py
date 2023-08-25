from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from .forms import CreateUserForm


def home_manager(request):
    # user = User.objects.create()
    return render(request,'manager/manager.html')

def create_team(request):
    return render(request,'manager/create_team.html')

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {"form": form}
    return render(request,'manager/register.html',context)
      

