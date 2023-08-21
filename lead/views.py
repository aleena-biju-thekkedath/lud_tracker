from django.shortcuts import render

# Create your views here.
def home_lead(request):
    return render(request,'lead/lead.html')
