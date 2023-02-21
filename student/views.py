from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view
from .serializers import StudentSerializer
from .models import Student
import jwt, datetime
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken


# def get_tokens_for_student(student):
#     refresh = RefreshToken.for_student(student)

#     return {
#         'refresh': str(refresh),
#         'access': str(refresh.access_token),
#     }


# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, student):
#         token = super().get_token(student)

#         # Add custom claims
#         token['email'] = student.email
#         token['role'] = student.role
#         # ...

#         return {email:email,token:token}


# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer


# class RegisterView(APIView):
class RegisterView(APIView):
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        student=serializer.save()
        tokenr = TokenObtainPairSerializer().get_token(student)  
        tokena = AccessToken().for_user(student)
        tokena['email'] = student.email
        tokena['role'] = student.role
        response = Response()
        response.data = {
            'student':serializer.data,
            'accessToken':str(tokena),
            'refreshToken': str(tokenr)
        }
        return response




class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        student = Student.objects.filter(email=email).first()
        if student is None:
            raise AuthenticationFailed('Student not found!')

        if not student.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        tokenr = TokenObtainPairSerializer().get_token(student)  
        tokena = AccessToken().for_user(student)
        tokena['email'] = student.email
        tokena['role'] = student.role
        response = Response()
        print("this is the response",response.data)
        response.set_cookie(key='jwt', value=tokena, httponly=True)
        response.data = {
            'id':student.id,
            'email':student.email,
            'accessToken':str(tokena),
            'refreshToken': str(tokenr)
        }
        return response


class getStudent(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        student = Student.objects.all()
        serializer = StudentSerializer(student,many=True)
        return Response(serializer.data)

class getStudentById(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request,id):
        student = Student.objects.get(id=id)
        serializer=StudentSerializer(student,many=False)
        return Response(serializer.data)

class updateStudent(APIView):
    # permission_classes = [IsAuthenticated]

    def patch(self, request,id):
        student = Student.objects.get(id=id)
        serializer=StudentSerializer(instance=student,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class deleteStudent(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request,id):
        student = Student.objects.get(id=id)
        student.delete()
        return Response("Item Successfully Deleted")

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response

class ValidateToken(APIView):
    def get(self, request):
        try:
            print("asdasdsadsadasdasd")
            token = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
            data=jwt.decode(token, "secret", algorithms=["HS256"])
            return Response(data)
        except Exception as e:
            return Response(e)
        
