from django.shortcuts import render

# Create your views here.
def home_member(request):
    return render(request,'member/member.html')

def login_page(request):
    return render(request,'member/login.html')