from django.contrib import admin
from django.urls import path, include
from .views import home_member

urlpatterns = [
    path("",home_member,name='member-home')
]