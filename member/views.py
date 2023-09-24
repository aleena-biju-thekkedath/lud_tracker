from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
def is_active_member(user):
    return user.is_active and not user.is_superuser


# @login_required
# @user_passes_test(is_active_member)
def home_member(request):
    return render(request,'member/member.html')

# @login_required
# @user_passes_test(is_active_member)
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
