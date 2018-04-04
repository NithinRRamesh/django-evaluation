from django.db import models

# Create your models here.

class employee(models.Model):
    employee_id = models.IntegerField()
    employee_name = models.CharField(max_length = 30)
    employee_department = models.CharField(max_length = 30)
    employee_sal = models.IntegerField()
    employee_dob = models.DateTimeField()
    employee_designation = models.CharField(max_length = 30,default="")