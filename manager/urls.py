from django.urls import path
from . import views

urlpatterns = [
    path("",views.home_manager,name='manager-home'),
    path("team/",views.create_team, name = 'manager-create'),
    path("modal/",views.modal, name = "manager-modal"),
    path("register/",views.register_single, name = "register"),
    path("register/csv/",views.process_uploaded_csv, name = "process_uploaded_csv"),

]