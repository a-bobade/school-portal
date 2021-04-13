from django.db import models


class Student(models.Model):
    matric = models.CharField(max_length=30, unique=True)
    lName = models.CharField(max_length=100)
    mName = models.CharField(max_length=100)
    fName = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    dob = models.CharField(max_length=30)
    email = models.EmailField()
    course = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    entry = models.CharField(max_length=30)
    exit = models.CharField(max_length=30)
    state = models.CharField(max_length=30)

