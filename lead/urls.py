from django.contrib import admin
from django.urls import path
from .views import home_lead,add_task,markTaskAsComplete

urlpatterns = [
    path("",home_lead,name='lead-home'),
    path("add/task",add_task,name='add_task'),
    path('mark/as/complete/<int:pk>/',markTaskAsComplete,name="markTaskAsComplete"),

]