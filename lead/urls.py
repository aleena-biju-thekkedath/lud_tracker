from django.contrib import admin
from django.urls import path
from .views import home_lead, try_lead

urlpatterns = [
    path("",home_lead,name='lead-home',),
    path("try/",try_lead,name='lead-try',),
]