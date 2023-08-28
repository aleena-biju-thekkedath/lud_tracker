from django.contrib.auth.models import User
from datetime import datetime
from django.db import models
from django.db.models import Max



class RangedIDField(models.PositiveIntegerField):
    def __init__(self, start_value, **kwargs):
        self.start_value = start_value
        kwargs['editable'] = False
        kwargs['unique'] = True
        kwargs['default'] = self._generate_next_value
        super().__init__(**kwargs)
    
    def _generate_next_value(self):
        max_id = self.model.objects.aggregate(max_id=Max(self.attname))['max_id']
        return max_id + 1 if max_id else self.start_value

class UserProfile(models.Model):
    current_datetime = datetime.now()
    current_date = current_datetime.year
    start_value = str("{}" + "000").format(current_date)
    emp_id = RangedIDField(start_value = start_value)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100) 
    # Add any other fields you need for the UserProfile



class Project(models.Model):
    proj_id =  RangedIDField(start_value=1000)
    proj_name = models.CharField(max_length= 100)
    proj_client = models.CharField(max_length = 100)
    proj_mgr_id = models.ForeignKey(UserProfile, on_delete = models.CASCADE, to_field = "emp_id", related_name = "proj_man_id")
    proj_status = models.CharField(max_length = 10)
    proj_startdate = models.DateField()
    proj_enddate = models.DateField()
    proj_lead_id = models.ForeignKey(UserProfile, on_delete = models.CASCADE, to_field = "emp_id",related_name = "proj_lead_id")
    proj_updated_start_date = models.DateField()
    proj_updated_end_date = models.DateField()

class Tasks(models.Model):
    date_created = models.DateTimeField()
    date_ended = models.DateTimeField()
    emp_id_assigned_to = models.ForeignKey(UserProfile, on_delete = models.CASCADE, to_field = "emp_id", related_name= "member_id")
    emp_id_assigned_by = models.ForeignKey(UserProfile, on_delete = models.CASCADE, to_field = "emp_id", related_name = "manger_id")   

class Members(models.Model):
    proj_id = models.ForeignKey(Project, on_delete = models.CASCADE, to_field = "proj_id", related_name = "ongoing_proj_id")
    emp_id = models.ForeignKey(UserProfile, on_delete = models.CASCADE, to_field = "emp_id",related_name = "emp_table_id")
    status = models.CharField(max_length= 10)
    date_joined = models.DateField()









