from django.db import models
from student.models import Student

class Applyleave(models.Model):
    id=models.AutoField(primary_key=True)
    studentId = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
    )
    startDate= models.DateField()
    endDate= models.DateField()
    status= models.BooleanField()

