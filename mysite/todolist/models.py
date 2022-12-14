from django.db import models

# Create your models here.

class Task(models.Model):
    def __str__(self):
        return self.task_name
    task_name = models.CharField(max_length=200)
    task_desc = models.CharField(max_length=500)
    task_status = models.BooleanField(default=False)
