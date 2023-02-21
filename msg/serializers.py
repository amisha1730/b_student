from rest_framework import serializers
from .models import Msg
from student.serializers import StudentSerializer
from student.models import Student


class CreateMsgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Msg
        fields = '__all__'

class ListMsgSerializer(serializers.ModelSerializer):
    
    student = StudentSerializer(read_only=True)
    class Meta:
        model = Msg
        fields = '__all__'



