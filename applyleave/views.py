from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CreateApplyleaveSerializer, ListApplyleaveSerializer
from .models import Applyleave
import jwt, datetime
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated,AllowAny


class createApplyleave(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        student= request.user
        request.data['student']=student.id
        serializer = CreateApplyleaveSerializer(data=request.data)
        serializer.student=student
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class getApplyleave(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        Applyleave = Applyleave.objects.all()
        serializer=ListApplyleaveSerializer(Applyleave,many=True)
        return Response(serializer.data)

class getApplyleaveById(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request,id):
        Applyleave = Applyleave.objects.get(id=id)
        serializer=ListApplyleaveSerializer(Applyleave,many=False)
        return Response(serializer.data)

class updateApplyleave(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request,id):
        Applyleave = Applyleave.objects.get(id=id)
        
        serializer=Applyleave(instance=Applyleave,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class approveleave(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request,id):
        Applyleave = Applyleave.objects.get(id=id)
        
        serializer=Applyleave(instance=Applyleave,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class deleteApplyleave(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request,id):
        Applyleave = Applyleave.objects.get(id=id)
        Applyleave.delete()
        return Response("Item Successfully Deleted")
