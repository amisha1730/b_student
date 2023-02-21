from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view

import jwt, datetime
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
import requests
import json

class getTeacher(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        teacher = requests.get('http://localhost:8081/teacher/get')
        response=json.loads(teacher.text)
        return Response(response)

class getTeacherById(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request,id):
        teacher = requests.get(f'http://localhost:8081/teacher/get/{id}')
        response=json.loads(teacher.text)
        return Response(response)

