from django.db import models

# Create your models here.

class database (models.Model):
    task_title = models.CharField(max_length=20)
    task_description = models.TextField()
    endtime = models.TimeField(default="00.00")