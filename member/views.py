from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages


# Create your views here.
def is_active_member(user):
    return user.is_active and not user.is_superuser


# @login_required
# @user_passes_test(is_active_member)
def home_member(request):
    try:
        member = request.user
        # print("Member Id: ", member)
        project = Member_Project_Status.objects.get(emp_id=member)

        task_list = Tasks.objects.filter(emp_id_assigned_to_id=project)
        # print(task)

        # task_title = task.title
        # print(task_title)
        # task_description = task.description
        # print(task_description)
        # task_start_date = task.date_created
        # print(task_start_date)
        # task_end_date = task.date_ended
        # print(task_end_date)


    except Tasks.DoesNotExist:
        # Handle the case where the project does not exist
        task_title = None
        task_description = None
        task_start_date = None
        task_end_date = None

    return render(request, "member/member.html", {"task_list": task_list})



# @login_required
# @user_passes_test(is_active_member)
def comments(request):
    return render(request, "comments.html")


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        print(user)

        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect("manager-home")
            elif user.is_staff:
                login(request, user)
                return redirect("lead-home")
            else:
                login(request, user)
                return redirect("member-home")
        else:
            messages.error(request, "Invalid username or password. Please try again.")

    return render(request, "member/login.html")


from django.shortcuts import render
from manager.models import User, Project, Tasks, Member_Project_Status


# def task_details(request):
    # Retrieve the project description based on the project_id
    # try:
    #     member = request.user
    #     print("Member Id: ", member)
    #     project = Member_Project_Status.objects.get(emp_id=member)

    #     task = Tasks.objects.get(emp_id_assigned_to_id=project)
    #     print(task)

    #     # task_title = task.title
    #     # print(task_title)
    #     # task_description = task.description
    #     # print(task_description)
    #     # task_start_date = task.date_created
    #     # print(task_start_date)
    #     # task_end_date = task.date_ended
    #     # print(task_end_date)

    # except Tasks.DoesNotExist:
    #     # Handle the case where the project does not exist
    #     task_title = None
    #     task_description = None
    #     task_start_date = None
    #     task_end_date = None

    # return render(request, "member/member.html", {"task": task})

def markTaskAsDone(request,pk):
    TaskObj=Tasks.objects.get(id=pk)
    TaskObj.task_status=1
    TaskObj.save()
    return redirect('member-home')
