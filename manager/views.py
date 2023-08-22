from django.shortcuts import render

# Create your views here.
def home_manager(request):
    return render(request,'manager/manager.html')


