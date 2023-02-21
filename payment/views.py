from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CreatePaymentSerializer, ListPaymentSerializer
from .models import Payment
import jwt, datetime
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated,AllowAny


class createPayment(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        student= request.user
        request.data['student']=student.id
        serializer = CreatePaymentSerializer(data=request.data)
        serializer.student=student
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class getPayment(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        Payment = Payment.objects.all()
        serializer=ListPaymentSerializer(Payment,many=True)
        return Response(serializer.data)

class getPaymentById(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request,id):
        Payment = Payment.objects.get(id=id)
        serializer=ListPaymentSerializer(Payment,many=False)
        return Response(serializer.data)

class updatePayment(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request,id):
        Payment = Payment.objects.get(id=id)
        
        serializer=CreatePaymentSerializer(instance=Payment,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class deletePayment(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request,id):
        Payment = Payment.objects.get(id=id)
        Payment.delete()
        return Response("Item Successfully Deleted")

