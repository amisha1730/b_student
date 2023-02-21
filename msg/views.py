from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CreateMsgSerializer, ListMsgSerializer
from .models import Msg
import jwt, datetime
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated,AllowAny


class createMsg(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        student= request.user
        request.data['student']=student.id
        serializer = CreateMsgSerializer(data=request.data)
        serializer.student=student
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class getMsg(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        Msg = Msg.objects.all()
        serializer=ListMsgSerializer(Msg,many=True)
        return Response(serializer.data)

class getMsgById(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request,id):
        Msg = Msg.objects.get(id=id)
        serializer=ListMsgSerializer(Msg,many=False)
        return Response(serializer.data)

class getMsgByTeacherId(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request,id):
        Msg = Msg.objects.get(teacherId=id)
        serializer=ListMsgSerializer(Msg,many=False)
        return Response(serializer.data)

class updateMsg(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request,id):
        Msg = Msg.objects.get(id=id)
        
        serializer=CreateMsgSerializer(instance=Msg,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class deleteMsg(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request,id):
        Msg = Msg.objects.get(id=id)
        Msg.delete()
        return Response("Item Successfully Deleted")



    
