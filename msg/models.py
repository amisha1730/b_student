from django.db import models

# Create your models here.
from student.models import Student

# Create your models here.
class Msg(models.Model):
    id=models.AutoField(primary_key=True)
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
    )
    teacherId =models.IntegerField()
    message = models.CharField(max_length=255)
    
    
