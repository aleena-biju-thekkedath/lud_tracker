from django.contrib.auth.models import User
from datetime import datetime
from django.db import models
from django.db.models import Max


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100) 
    # Add any other fields you need for the UserProfile


class Project(models.Model):
    proj_name = models.CharField(max_length= 100)
    proj_client = models.CharField(max_length = 100)
    proj_mgr_id = models.ForeignKey(UserProfile, on_delete = models.CASCADE, related_name = "proj_man_id")
    proj_status = models.CharField(max_length = 10)
    proj_startdate = models.DateField()
    proj_enddate = models.DateField()
    proj_lead_id = models.ForeignKey(UserProfile, on_delete = models.CASCADE,related_name = "proj_lead_id")
    proj_updated_start_date = models.DateField()
    proj_updated_end_date = models.DateField()

class Tasks(models.Model):
    date_created = models.DateTimeField()
    date_ended = models.DateTimeField()
    emp_id_assigned_to = models.ForeignKey(UserProfile, on_delete = models.CASCADE, related_name= "member_id")
    emp_id_assigned_by = models.ForeignKey(UserProfile, on_delete = models.CASCADE, related_name = "manger_id")   

class Members(models.Model):
    proj_id = models.ForeignKey(Project, on_delete = models.CASCADE,)
    emp_id = models.ForeignKey(UserProfile, on_delete = models.CASCADE,)
    status = models.CharField(max_length= 10)
    date_joined = models.DateField()


    









