from rest_framework import serializers
from .models import Applyleave
from student.serializers import StudentSerializer
from student.models import Student


class CreateApplyleaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applyleave
        fields = '__all__'

class ListApplyleaveSerializer(serializers.ModelSerializer):
    
    student = StudentSerializer(read_only=True)
    class Meta:
        model = Applyleave
        fields = '__all__'



