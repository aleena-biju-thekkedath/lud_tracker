from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.hashers import make_password
from lud_tracker import settings
from .models import UserProfile
from django.contrib import messages


# For Manager Home Page: 
def home_manager(request):
    # user = User.objects.create()
    return render(request, 'manager/manager.html')


def modal(request):
    # user = User.objects.create()
    return render(request, 'manager/project_modal.html')

# Create Team Page :
def create_team(request):
    users = User.objects.all()
    print(users)
    return render(request,"manager/create_team.html",{'users': users})


# For Processing the Csv File uploaded by Manager: 
def process_uploaded_csv(request):
    if request.POST:
        uploaded_file = request.FILES["file"]
        filepath = "files/" + uploaded_file.name
        fs = FileSystemStorage()
        print(filepath)
        fs.save(filepath, uploaded_file)
        is_first_row = True  # Flag to track the first row
        # count = 0
        print(settings.MEDIA_ROOT)
        file_data = open(settings.MEDIA_ROOT + '/' + filepath, 'r')
        for line in file_data.readlines():
            if is_first_row:
                is_first_row = False
                continue  # Skip the first row

            fields = line.split(",")
            # print(fields[0])

            if fields[3].strip().lower() == "manager":
                user = User(username=fields[0], email=fields[1],
                        password=make_password(fields[2]),is_superuser =True)
                user.save()
            
            else:
                user = User(username=fields[0], email=fields[1],
                        password=make_password(fields[2]))
                user.save()
            
            
            userObj= UserProfile.objects.create(user=user,role=fields[3])
            userObj.save()

        return redirect('manager-home')
    else:
        return render(request, "manager/register.html")


# For Registering Single User: 
def register_single(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')  
        role = request.POST.get('role')
        
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('register')  # Redirect back to the form page
        
        if role.lower() == "manager":
            user = User.objects.create(username=name,email =email,password = password,is_superuser= True)
            user.save()
            userProfile = UserProfile.objects.create(role=role,user=user)
            userProfile.save()
            messages.success(request, "Profile Uploaded Successfully ")
            return redirect('register') 
            
        elif role.lower()== "member":
            user = User.objects.create(username = name,email =email,password = password)
            userProfile = UserProfile.objects.create(role=role,user=user)
            user.save()
            userProfile.save()
            messages.success(request, "Profile Uploaded Successfully ")
            return redirect(request, 'manager/register.html')
            
    return render(request, 'manager/register.html')



def project_details(request):
    if request.method == 'POST':
        user = request.user
        proj_name = request.POST.get('proj_name')
        proj_desc = request.POST.get('proj_desc')
        proj_start = request.POST.get('proj_start')
        proj_end= request.POST.get('proj_end') 
        proj_manager_id = user.id
        proj_lead_id = request.post.get()

from django.shortcuts import render




