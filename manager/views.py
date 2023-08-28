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
        # For The Date format of the file
        current_datetime = datetime.now()
        current_date = current_datetime.date()

        # Catching the Uploaded File: 
        uploaded_file = request.FILES["file"]
        filepath = "files/" + uploaded_file.name + "date_({})".format(str(current_date))  
        fs = FileSystemStorage()
        fs.save(filepath, uploaded_file)
        
         # Flag to track the first row
        is_first_row = True 

        # Opening the File for root directory: 
        file_data = open(settings.MEDIA_ROOT + '/' + filepath, 'r')

        # For skipping the Heading Column: 
        for line in file_data.readlines():
            if is_first_row:
                is_first_row = False
                continue 

            # Code for defining Fields
            fields = line.split(",")
            print(fields[0])

        # Defining the variables for each user object:
        user = UserProfile(username=fields[0],email=fields[1],password= make_password(fields[2]),role = fields[3])

        # Note : 
        # Create a AbstractUser table or append a column Role in User Table

        try:
            user = User.objects.get(username=fields[0])
            
            if user.fields[3] == 'manager':
                user.is_superuser = True
                user.is_staff = False
            elif user.fields[3] == 'lead':
                user.is_superuser = False
                user.is_staff = True
            else:
                user.is_superuser = False
                user.is_staff = False
            
            user.save()
  
        except user.fields[3] == "NA":
            pass

        return redirect('manager-home')
   else: 
       return render(request,"manager/record_upload.html")
   

  


      

