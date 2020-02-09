from django.db import models

# Create your models here.
class Student(models.Model):
    StudentId=models.CharField(max_length=50)
    StudentName=models.CharField(max_length=50)
    Age=models.IntegerField()
