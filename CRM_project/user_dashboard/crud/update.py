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


class UserUpdate(generics.GenericAPIView):
    serializer_class =regserialzer
    # permission_classes = [IsAdminUser]   
    def get(self, request,id):
        user = Account.objects.get(id=id)
        response = returnresponse(status_code=200,data=regserialzer(user).data, message='Success')
        return Response(response)
    
    def delete(self,request,id):
       user = Account.objects.get(id=id).delete()
       response = returnresponse(status_code=200,data="deleted",message="success")
       return Response(response)
    
    def put(self,request,id):
      user = Account.objects.get(id=id)
      user.name = request.data.get('name')
      user.email=request.data.get('email')
      user.password = request.data.get('password')
      user.role = request.data.get('role')
      user.save()
      #    print("--------------------------------",user)
      #    ser = regserialzer(instance=user,data=request.data)
      #    ser.is_valid()
      #    ser.save()
      #    print(ser.data)
      #    print(user.email)
      response = returnresponse(status_code=200,data=regserialzer(user).data,message="Success")
      return Response(response)
