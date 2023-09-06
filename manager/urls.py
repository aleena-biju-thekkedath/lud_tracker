from django.urls import path
from . import views

urlpatterns = [
    path("",views.home_manager,name='manager-home'),
<<<<<<< HEAD
    path("team/",views.create_team, name= 'manager-create'),
=======
    path("team/",views.team_project_details, name = 'manager-create'),
>>>>>>> 5779e9e9f6913fe9bd6a7c3cd59d29789d2f66cd
    path("modal/",views.modal, name = "manager-modal"),
    path("register/",views.register_single, name = "register"),
    path("register/csv/",views.process_uploaded_csv, name = "process_uploaded_csv"),

]