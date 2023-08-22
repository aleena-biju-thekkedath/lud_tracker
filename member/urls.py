from django.contrib import admin
from django.urls import path, include
from .views import home_member,login_page

urlpatterns = [
    path("members/ ",home_member,name='member-home'),
    path("",login_page,name='login-page'),
]