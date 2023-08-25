from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .utils import process_csv_data
# from django.contrib.auth.forms import UserCreationForm


# Create your views here.
# from .forms import CreateUserForm


def home_manager(request):
    # user = User.objects.create()
    return render(request,'manager/manager.html')

def create_team(request):
    return render(request,'manager/create_team.html')

def register(request):
    csv_url = "static/login_data.csv"
    process_csv_data(csv_url)
    return render(request,"manager/manager.html")
    # form = CreateUserForm()
    # if request.method == "POST":
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    # context = {"form": form}
    # return render(request,'manager/register.html',context)
    # In your app's views.py

  


      

