from django.urls import path
from . import views

urlpatterns = [
    path("manager/",views.home_manager,name='manager-home'),
    path("team/",views.create_team, name = 'manager-create'),
    path("register/",views.register, name = "manager-register"),
    
]