from django.shortcuts import render, redirect
from manager.models import Tasks, UserProfile,Project,Member_Project_Status
from django.contrib.auth.models import User 
from django.contrib import messages
import re
# from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
def is_staff(user):
    return user.is_staff 

# @login_required 
# @user_passes_test(is_staff)
def home_lead(request):
    lead=request.user
    projectObj=Project.objects.get(proj_lead_id=lead)
    members_list=Member_Project_Status.objects.filter(project_id=projectObj)
    return render(request,'lead/lead1.html',{"members_list": members_list})

# @login_required 
# @user_passes_test(is_staff)
# def try_lead(request):
#     tasks = Tasks.objects.all() 
#     return render(request,'lead/try.html',{"tasks":tasks})

# @login_required 
# @user_passes_test(is_staff)
def add_task(request): 
    tasks = Tasks.objects.all()
    lead=request.user
    projectObj=Project.objects.get(proj_lead_id=lead)
    members_list=Member_Project_Status.objects.filter(project_id=projectObj,status=1)
    print(members_list)
    print(tasks)
    if request.method == 'POST':
        # lead = request.user
        lead_id = lead
        member = request.POST.get('selected_username')
        memberObj=Member_Project_Status.objects.get(id=member)

        task_title = request.POST.get('task_title')
        task_desc = request.POST.get('task_description')
        task_start = request.POST.get('start_date')
        task_end= request.POST.get('end_date') 

        # member = re.sub(r'[^0-9]', '', member)
        # member_id = re.sub(r'\s+', '', member)
        # member_id = int(member_id)
       
        
        # if member == "Not Assigned": 
        # # Retrieve the user based on the selected username
        #     task_details = Tasks.objects.create(date_created = task_start,
        #                                         date_ended = task_end,
        #                                         emp_id_assigned_to = member,  
        #                                         task_status = 1, 
        #                                         task_description = task_desc,
        #                                         task_title = task_title)
        
         
        task_details = Tasks.objects.create(date_created = task_start,
                                           date_ended = task_end,
                                           emp_id_assigned_to = memberObj,  
                                           task_status = 1, 
                                           task_description = task_desc,
                                           task_title = task_title)

        task_details.save()
        messages.success(request, "Task Assigned Successfully..")
        return redirect("lead-home")
    return render(request,'lead/lead1.html', {"members_list": members_list})

# @login_required 
# @user_passes_test(is_staff)    
def update_task_dates(request): 
    tasks = Tasks.objects.all()
    task_name = request.POST.get('project_name')
    task_id = request.POST.get('project_id')
    existing_start = Tasks.objects.get(tasks.date_created,id = task_id)
    existing_end = Tasks.objects.get(tasks.date_enddate,id = task_id)
    print(f"Project Dates are /n Start Date: {existing_start} /n End Date: {existing_end} ")
    updated_start = request.POST.get('updated_start_date')
    updated_end = request.POST.get('updated_end_date')

    try:
        if tasks.id == task_id or tasks.name == task_name:
        # Replace with the Updated Dates : 
            tasks.updated_startdate = updated_start 
            tasks.updated_enddate = updated_end
            tasks.save()
        
    except tasks.id == Tasks.DoesNotExist:
        # Handle the case where the project does not exist
        messages.error(request, "Task Not Found ... Please Try Again")
        return redirect("lead-try")
    
    # Check if the name is null and update it to a non-null value
    else: 
        messages.success(request, "Task Dates Updated Successfully")
        return redirect("lead-try")
    
    

# @login_required 
# @user_passes_test(is_staff)
def try_lead(request):
    tasks = Tasks.objects.all() 
    users = User.bjects.all()
    return render(request,'lead/lead1.html',{"tasks":tasks, "users": users })

# @login_required 
# @user_passes_test(is_staff)

    


                  
            