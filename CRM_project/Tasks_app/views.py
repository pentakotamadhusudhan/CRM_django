from django.shortcuts import render
# from ..modules import *
from .models import *
from .serializers import *
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.views import APIView
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from rest_framework import generics
from rest_framework import permissions
from GenericResponse import returnresponse


from django.contrib.auth.hashers import make_password, check_password

# Create your views here.


class CreateTasks(generics.ListCreateAPIView):
    serializer_class=task_serializer
    queryset = TaskModels.objects.all()
    permission_classes = (IsAdminUser,IsAuthenticated )    



class CreateTasks(APIView):
    permission_classes = (IsAuthenticated, )    
    serializer_class =task_serializer

    def post(self, request):
        try:
            ser = task_serializer(data=request.data)
            ser.is_valid()
            ser.save()
            response = returnresponse()
            return Response(ser.data)
        except : 
            return Response("error occuer")
    def get(self,request):
        try:
            user  = TaskModels.objects.all()
            ser = task_serializer(data=user,many=True)
            ser.is_valid()
            return Response({"result":ser.data})
        except Exception as e:
            return Response({
                "Result":e
            })
    def put(self, request,id):
        try:
            ser = task_serializer(data=request.data)
            ser.is_valid()
            ser.save()
            return Response(ser.data)
        except : 
            return Response("error occuer")
        
    