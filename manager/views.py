from django.shortcuts import render

# Create your views here.
def home_manager(request):
    return render(request,'manager/manager.html')

def create_team(request):
    return render(request,'manager/create_team.html')

def calendar(request):
    return render(request,'manager/calendar.html')

def project_modal(request):
    return render(request,'manager/project_modal.html')


