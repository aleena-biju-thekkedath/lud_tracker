from django.urls import path
from .views import home_member,login_page, comments,markTaskAsDone
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("members/",home_member,name='member-home'),
    path("",login_page,name='login-page'),
    path("comments/",comments,name='comments'),
    path("logout/",LogoutView.as_view(),name='logout'),
    # path("get_task_details/", task_details, name = "task-details")
    path('mark/as/done/<int:pk>/',markTaskAsDone,name="markTaskAsDone"),
    

]