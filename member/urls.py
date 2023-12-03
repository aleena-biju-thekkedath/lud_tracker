from django.urls import path
from .views import home_member,login_page, comments

urlpatterns = [
    path("members/",home_member,name='member-home'),
    path("",login_page,name='login-page'),
    path("comments/",comments,name='comments'),
    
]