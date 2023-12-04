from django.contrib.auth.models import User
from django.db import models


# UserProfile Model for User Information: 
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100) 


class Project(models.Model):    
    proj_name = models.CharField(max_length= 100)
    proj_mgr_id = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "proj_man_id")
    proj_status = models.CharField(max_length = 10)
    proj_startdate = models.DateField()
    proj_enddate = models.DateField()
    proj_lead_id = models.ForeignKey(User, on_delete = models.CASCADE,related_name = "proj_lead_id")
    # proj_updated_start_date = models.DateField()
    # proj_updated_end_date = models.DateField()
    proj_desc = models.CharField(max_length = 1000,default= "NA")


class Member_Project_Status(models.Model):
    project_id = models.ForeignKey(Project, on_delete = models.CASCADE,)
    emp_id = models.ForeignKey(User, on_delete = models.CASCADE,)
    status = models.BooleanField(default=0) 
    date_joined = models.DateField(auto_now_add=True)

# Task Database for Task Information: 
class Tasks(models.Model):
    date_created = models.DateTimeField()
    date_ended = models.DateTimeField()
    emp_id_assigned_to = models.ForeignKey(Member_Project_Status, on_delete = models.CASCADE,)
    task_status = models.IntegerField(default=0) 
    task_description = models.CharField(max_length = 1000, default = "NA")
    task_title = models.CharField(max_length = 100, default = "NA")
    # updated_startdate = models.DateField(default = None)                               
    # updated_enddate = models.DateField(default = None)                               



