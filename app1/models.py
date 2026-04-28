from django.db import models

class Student(models.Model):
    Name = models.CharField(max_length=100)
    age = models.IntegerField()
    Course = models.CharField(max_length=100)


    def __str__(self):
     return self.Name
