from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CreateStudentDetailSerializer,ListStudentDetailSerializer
from .models import StudentDetail
import jwt, datetime
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated,AllowAny


class createStudentDetail(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        student= request.user
        request.data['student']=student.id
        serializer = CreateStudentDetailSerializer(data=request.data)
        serializer.student=student
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class getStudentDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        studentDetail = StudentDetail.objects.all()
        serializer=ListStudentDetailSerializer(studentDetail,many=True)
        return Response(serializer.data)

class getStudentDetailById(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request,id):
        studentDetail = StudentDetail.objects.get(id=id)
        serializer=ListStudentDetailSerializer(studentDetail,many=False)
        return Response(serializer.data)

class updateStudentDetail(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request,id):
        print("la la la ra la la")
        studentDetail = StudentDetail.objects.get(id=id)
        
        serializer=CreateStudentDetailSerializer(instance=StudentDetail,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class deleteStudentDetail(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request,id):
        studentDetail = StudentDetail.objects.get(id=id)
        studentDetail.delete()
        return Response("Item Successfully Deleted")



    