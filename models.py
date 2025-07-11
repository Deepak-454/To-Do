from django.db import models

class Todo(models.Model):
    todo=models.CharField(max_length=70)
    priority=models.CharField(max_length=10,default="medium")
