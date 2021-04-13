from django.db import models


class Results(models.Model):
    matric = models.CharField(max_length=30)
    code = models.CharField(max_length=10)
    ca1 = models.IntegerField()
    ca2 = models.IntegerField()
    exam = models.IntegerField()
    mark = models.IntegerField()
    level = models.IntegerField()
    semester = models.IntegerField()
    session = models.CharField(max_length=20)
    trials = models.IntegerField()
