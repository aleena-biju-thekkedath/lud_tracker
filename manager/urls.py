from django.urls import path
from . import views

urlpatterns = [
    path("",views.home_manager,name='manager-home'),
    path("team/",views.create_team, name = 'manager-create'),
    path("calendar/",views.calendar, name = "manager-calendar")
]