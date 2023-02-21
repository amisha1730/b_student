from rest_framework import serializers
from .models import StudentDetail
from student.serializers import StudentSerializer
from student.models import Student


class CreateStudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetail
        fields = '__all__'

class ListStudentDetailSerializer(serializers.ModelSerializer):
    
    student = StudentSerializer(read_only=True)
    class Meta:
        model = StudentDetail
        fields = '__all__'


