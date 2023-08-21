from django.shortcuts import render

# Create your views here.
def home_member(request):
    return render(request,'member/member.html')