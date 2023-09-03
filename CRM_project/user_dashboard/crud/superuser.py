import json
from django.contrib.auth import get_user_model
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from ..serializers import *
from ..models import Login
from GenericResponse import returnresponse
from django.contrib.auth.hashers import make_password, check_password




class SuperUser(generics.CreateAPIView):
    serializer_class = SuperAdminserializer
    query_set = User.objects.all()
    permission_classes = [IsAdminUser,]   


    def post(self, request):
        try:
           user = User()
           user.email= request.data.get('email')
           user.username= request.data.get('username')
           user.password= make_password(request.data.get('password'))
           user.first_name= request.data.get('first_name')
           user.last_name   = request.data.get('last_name')
           user.save()
           response = returnresponse(status_code=status.HTTP_200_OK,data=SuperAdminserializer(user).data,message="Success")
           return Response(response)
        except Exception as e: 
            response = returnresponse(status_code=status.HTTP_400_BAD_REQUEST,data=[],message="Failed")
            return Response(response)

    def get(self,request):
        try:
            user  = User.objects.all()
            ser = SuperAdminserializer(data=user,many=True)
            ser.is_valid()
            # print(ser)
            response = returnresponse(status_code=status.HTTP_100_CONTINUE,data=ser.data,message="Success")
            return Response(response)
        except:
            response = returnresponse(status_code=status.HTTP_400_BAD_REQUEST,data=[],message='failed')
            return Response(response)
            
