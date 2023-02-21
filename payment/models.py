from django.db import models
from student.models import Student

# Create your models here.
class Payment(models.Model):
    id=models.AutoField(primary_key=True)
    studentId = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
    )
    paymentdate = models.DateField()
    paymentamount = models.IntegerField()
    
