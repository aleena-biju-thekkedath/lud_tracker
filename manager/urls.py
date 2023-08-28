from django.urls import path
from . import views

urlpatterns = [
    path("",views.home_manager,name='manager-home'),
    path("team/",views.create_team, name = 'manager-create'),
    path("record_mandate/",views.process_uploaded_csv, name = "manager-records"),
    
]