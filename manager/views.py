from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.hashers import make_password
from lud_tracker import settings
from .models import UserProfile, Project
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

# from django.urls import reverse_lazy
from django.http import HttpResponse


# ----------------------------------------Check if the user is a superuser  ---------------------------------------------
def is_admin(user):
    return user.is_superuser


# ------------------------------------------ Manager Home Page View  ---------------------------------------------
# Ensure the user is logged in
def home_manager(request):
    # user = User.objects.create()
    return render(request, "manager/manager.html")


def modal(request):
    # user = User.objects.create()
    return render(request, "manager/project_modal.html")


# ========For Manager Register Page =======================================================================================
# Status : Completed


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
        file_data = open(settings.MEDIA_ROOT + "/" + filepath, "r")
        for line in file_data.readlines():
            if is_first_row:
                is_first_row = False
                continue  # Skip the first row

            fields = line.split(",")
            # print(fields[0])
            hasedpassword = make_password(fields[3])
            print(hasedpassword)

            if fields[3].strip().lower() == "manager":
                user = User(
                    username=fields[1],
                    email=fields[2],
                    password=hasedpassword,
                    first_name=fields[4],
                    is_superuser=True,
                )
                user.save()
            else:
                user = User(
                    username=fields[1],
                    email=fields[2],
                    password=hasedpassword,
                    first_name=fields[4],
                )
                user.save()

            userObj = UserProfile.objects.create(user=user, role=fields[5])
            userObj.save()

        return redirect("manager-home")
    else:
        return render(request, "manager/register.html")


# # For Registering Single User:
# ------------------------------------


def register_single(request):
    if request.method == "POST":
        username = request.POST.get("username")
        first_name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        role = request.POST.get("role")

        # Password Cross Checking Step:
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect("register")  # Redirect back to the form page

        # Role Checking Code for assigning user permissions:
        if role.lower() == "manager":
            user = User.objects.create(
                username=username,
                email=email,
                password=make_password(password),
                is_superuser=True,
                is_staff=True,
                first_name=first_name,
            )
            user.save()
            userProfile = UserProfile.objects.create(role=role, user=user)
            userProfile.save()
            messages.success(request, "Profile Uploaded Successfully ")
            return redirect("register")

        elif role.lower() == "member":
            user = User.objects.create(
                username=username,
                email=email,
                password=make_password(password),
                first_name=first_name,
            )
            userProfile = UserProfile.objects.create(role=role, user=user)
            user.save()
            userProfile.save()
            messages.success(request, "Profile Uploaded Successfully ")
            return redirect("register")

    return render(request, "manager/register.html")


# ==================================================================================================================


# # ===================================== Project Details for The Manager ===========================================
# Status:


def team_project_details(request):
    users = User.objects.all()
    user_profile = UserProfile.objects.all()
    current_user = request.user
    # all_Assigned_members = Member_Project_Status.objects.all()
    # all_Assigned_members.save()
    if request.method == "POST":
        # Assuming you want to get the logged-in user

        proj_name = request.POST.get("proj_name")
        proj_desc = request.POST.get("proj_desc")
        proj_start = request.POST.get("proj_start")
        proj_end = request.POST.get("proj_end")

        lead_id = request.POST.get("team_lead_username")
        print('lead_id :',lead_id)
        lead = User.objects.get(id=lead_id)

        project_details = Project.objects.create(
                    proj_name=proj_name,
                    proj_desc=proj_desc,
                    proj_mgr_id=current_user,
                    proj_status=True,  # Assuming you want to set the status to "Active"
                    proj_startdate=proj_start,
                    proj_enddate=proj_end,  
                    proj_lead_id=lead,
                )
                # Save the project
        project_details.save()
        print('project_details id:',project_details.id)

        user_list = request.POST.getlist("select_members")
        print(user_list)
        for user in user_list:
                    userObj = User.objects.get(id=user)
                    teamMemberObj = Member_Project_Status.objects.create(
                        project_id=project_details, emp_id=userObj, status=1
                    )
        teamMemberObj.save()

        all_Assigned_members = Member_Project_Status.objects.all()

        # Fix the typo: should be request.POST.get, not request.post.get

        for mem in all_Assigned_members:
            if mem.status == 0:
                lead.is_staff = True
                lead.save()

                # Create the project object
                # project_details = Project.objects.create(
                #     proj_name=proj_name,
                #     proj_desc=proj_desc,
                #     proj_mgr_id=current_user,
                #     proj_status=True,  # Assuming you want to set the status to "Active"
                #     proj_startdate=proj_start,
                #     proj_enddate=proj_end,  
                #     proj_lead_id=lead,
                # )

                # # Save the project
                # project_details.save()
                # print('project_details id:',project_details.id)

                # user_list = request.POST.getlist("select_members")
                # print(user_list)
                # for user in user_list:
                #     userObj = User.objects.get(id=user)
                #     teamMemberObj = Member_Project_Status.objects.create(
                #         project_id=project_details, emp_id=userObj, status=1
                #     )
                # teamMemberObj.save()
                messages.success(request, "Project Assigned Successfully")
                return redirect("manager-home")
            else:
                messages.error(request, "Team lead is already assigned to a Project")
        return redirect("manager-home")
    else:
        return render(
            request,
            "manager/create_team.html",
            {"users": users, "user_profile": user_profile,"manager": current_user.username},
        )



from django.shortcuts import render, redirect
from .models import Member_Project_Status
from django.contrib import messages


def confirm_completion(request, project_id):
    if request.method == "POST":
        # Assuming you have a form with a button that submits to this view
        proj_title = request.POST.get(name="project-title")

        project = Project.objects.get(proj_title=proj_title)
        project_id = project.id

        try:
            # Get all Member_Project_Status objects with the given project_id
            members_statuses = Member_Project_Status.objects.filter(
                project_id=project_id
            )

            # Update the status to "completed" for all objects
            members_statuses.update(status="completed")

            messages.success(request, "Confirmation of completion successful.")
            return redirect("manager-home")

        except Member_Project_Status.DoesNotExist:
            messages.error(request, "Member_Project_Status does not exist.")
            return redirect("manager-home")

    else:
        messages.error(request, "Invalid request method.")
        return redirect("manager-home")


# ==================================================================================================================
