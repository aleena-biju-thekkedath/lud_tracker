from django.shortcuts import render, redirect
from django.db import models
from django.contrib.auth.models import User 
from .models import Project
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.hashers import make_password
from lud_tracker import settings
from .models import UserProfile, Project, Tasks
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
# from django.urls import reverse_lazy
from django.http import HttpResponse



# Check if the user is a superuser
def is_admin(user):
    return user.is_superuser  


# For Manager Home Page: 
 # Ensure the user is logged in
# @login_required 
# @user_passes_test(is_admin)
def home_manager(request):
    # user = User.objects.create()
    return render(request, 'manager/manager.html')

# @login_required 
# @user_passes_test(is_admin)
def modal(request):
    # user = User.objects.create()
    return render(request, 'manager/project_modal.html')

# Create Team Page :



# For Processing the Csv File uploaded by Manager: 
# @login_required 
# @user_passes_test(is_admin)
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
# @login_required 
# @user_passes_test(is_admin)
def register_single(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')  
        role = request.POST.get('role')
        
        # Password Cross Checking Step: 
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('register')  # Redirect back to the form page
        
        # Role Checking Code for assigning user permissions: 
        if role.lower() == "manager":
            user = User.objects.create(username=username,email =email,password = make_password(password),is_superuser= True,first_name = name)
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
            return redirect('register')
            
    return render(request, 'manager/register.html')

# @login_required 
# @user_passes_test(is_admin)
def team_project_details(request):
    users = User.objects.all()
    print(users)
    if request.method == 'POST':
        manager = request.user
        manager_id = manager.id
        proj_name = request.POST.get('proj_name')
        proj_desc = request.POST.get('proj_desc')
        proj_start = request.POST.get('proj_start')
        proj_end= request.POST.get('proj_end') 
        proj_lead_id = request.post.get()
        lead_name = request.POST.get('team-lead-username')
        user = User.objects.get(username = lead_name)
        
        proj_lead_id = user.id
        project_client = "CHRIST University"
        # Retrieve the user based on the selected username
        project_details = Project.objects.create(proj_name =proj_name,
                                                 proj_desc = proj_desc,
                                                proj_client = project_client,
                                                proj_manager_id = manager_id,
                                                proj_status = "Active", 
                                                proj_startdate = proj_start,
                                                proj_enddate = proj_end,
                                                proj_lead_id = proj_lead_id,
                                                proj_updated_start_date = models.SET_NULL,
                                                proj_updated_end_date = models.SET_NULL) 
        
        project_details.save()
        messages.success(request, "Task Assigned Successfully..")
        return redirect("manager-create")
    
    else:
        return render(request,"manager/create_team.html",{'users': users})
    
# @login_required 
# @user_passes_test(is_admin)
def update_project_dates(request): 
        project_name = request.POST.get('project_name')
        project_id = request.POST.get('project_id')
        existing_start = Project.objects.get(project.proj_startdate,id = project_id)
        existing_end = Project.objects.get(project.proj_enddate,id = project_id)
        print(f"Project Dates are /n Start Date: {existing_start} /n End Date: {existing_end} ")
        updated_start = request.POST.get('updated_start_date')
        updated_end = request.POST.get('updated_end_date')

        try:
            project = Project.objects.get(id=project_id)
        except Project.DoesNotExist:
                # Handle the case where the project does not exist
                messages.error(request, "Project Not Found ... Please Try Again")
                return redirect("manager-create")
            
            # Check if the name is null and update it to a non-null value
        if project.id == project_id or project.name == project_name:
                # Replace with the Updated Dates : 
            project.proj_updated_start_date = updated_start 
            project.proj_updated_end_date = updated_end
            project.save()

            messages.success(request, "Project Dates Updated Successfully")
            return redirect("manager-create")


    # Replace 'other_page_name' with the name of the page you want to redirect unauthorized users to.
def unauthorized_access(request):
    return HttpResponse("<h1> You are not authorized to view this page. Refresh or return to home page !! </h1>") 
