from django.contrib import admin
from django.urls import path
from .views import home_lead

urlpatterns = [
    path("",home_lead,name='lead-home'),

]