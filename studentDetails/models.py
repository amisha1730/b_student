from django.db import models
from student.models import Student


class StudentDetail(models.Model):
    id=models.AutoField(primary_key=True)
    contact= models.CharField(max_length=255)
    address= models.CharField(max_length=255)
    additionalInfo= models.CharField(max_length=255)
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
    )
