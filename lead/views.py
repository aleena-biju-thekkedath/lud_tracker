from django.shortcuts import render

# Create your views here.
def home_lead(request):
    return render(request,'lead/lead.html')

def try_lead(request):
    return render(request,'lead/try.html')