from rest_framework import serializers
from .models import Payment
from student.serializers import StudentSerializer
from student.models import Student


class CreatePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class ListPaymentSerializer(serializers.ModelSerializer):
    
    student = StudentSerializer(read_only=True)
    class Meta:
        model = Payment
        fields = '__all__'



