from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login

# Create your views here.
def home_member(request):
    return render(request,'member/member.html')

def comments(request):
    return render(request,'comments.html')

def login_page(request):
    if request.method=='POST':
        username =request.POST.get('Username')
        password =request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is super:
            login(request,user)
            return redirect('member -home')
        else:
            return render(request,'member/login.html')

    else : 
        return render(request,'member/login.html')
