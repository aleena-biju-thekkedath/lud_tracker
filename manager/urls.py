from django.urls import path
from . import views

urlpatterns = [
    path("",views.home_manager,name='manager-home')
]