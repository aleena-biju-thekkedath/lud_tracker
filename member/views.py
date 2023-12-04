from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

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
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        print(user)

        if user is not None:
            
            if user.is_superuser:
                login(request, user)
                return redirect('manager-home')
            elif user.is_staff:
                login(request, user)
                return redirect('lead-home')
            else:
                login(request, user)
                return redirect('member-home')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')

    return render(request, 'member/login.html')