from django.db import models
from datetime import datetime

# Create your models here.
class Task(models.Model):
    task=models.CharField(max_length=300)
    