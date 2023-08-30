from django.shortcuts import render,redirect
import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from datetime import datetime
from django.shortcuts import render
# from django.utils.timezone import get_current_timezone
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.hashers import make_password
from lud_tracker import settings
from django.http import HttpResponse
from .models import UserProfile
# from django.contrib.auth.forms import UserCreationForm


# Create your views here.
from .forms import CreateUserForm


def home_manager(request):
    # user = User.objects.create()
    return render(request, 'manager/manager.html')


def create_team(request):
    return render(request, 'manager/create_team.html')


def process_uploaded_csv(request):
    if request.POST:
        # if request.user.is_superuser:
        uploaded_file = request.FILES["file"]
        filepath = "files/" + uploaded_file.name
        fs = FileSystemStorage()
        fs.save(filepath, uploaded_file)
        is_first_row = True  # Flag to track the first row
        # count = 0
        # print(settings.MEDIA_ROOT)
        file_data = open(settings.MEDIA_ROOT + '/' + filepath, 'r')
        for line in file_data.readlines():
            if is_first_row:
                is_first_row = False
                continue  # Skip the first row

            fields = line.split(",")
            print(fields[0])
            user = User(username=fields[0], email=fields[1],
                        password=make_password(fields[2]))
            user.save()

        return redirect('manager-home')
    else:
        return render(request, "manager/register.html")
   
def register(request):
    form = CreateUserForm()
    if request.POST:
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, 'manager/register.html', context)

  


      

