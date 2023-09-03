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


User = get_user_model()
class RegisterView(generics.GenericAPIView):
    serializer_class = regserialzer
    
    def post(self, request):
        try:
            ser = regserialzer(data=request.data)
            ser.is_valid()
            ser.save()
            response = returnresponse(200,ser.data,"success")
            return Response(response)
        except : 
            response = returnresponse(400,'error occured while creating',"Failed")
            return Response(response)
    def get(self,request):
        
        user = Account.objects.all()
        ser = regserialzer(data=user, many=True)
        ser.is_valid()
        response  = returnresponse(200,ser.data,"success")
        return Response(response)