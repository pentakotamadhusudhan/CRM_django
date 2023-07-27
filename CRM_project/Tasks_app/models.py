from django.db import models

# Create your models here.

taskstatus  = [
  ("Craeted", "Craeted"),
  ("Pending", "Pending"),
  ("OverDue", "OverDue"),
  ("Done", "Done"),


]


class TaskModels(models.Model):
    task_name = models.CharField(max_length=100)
    task_description = models.TextField()
    assign_to = models.CharField(max_length=1000)
    task_status = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True)
    updated_on = models.DateTimeField(auto_now=True)
    object = models.manager
