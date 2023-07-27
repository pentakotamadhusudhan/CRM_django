import json
from django.contrib.auth import get_user_model
from django.http import JsonResponse
User = get_user_model()
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .serializers import *
from .models import Login
from GenericResponse import returnresponse
from django.contrib.auth.hashers import make_password, check_password

class RegisterView(APIView):
    permission_classes = (IsAdminUser,IsAuthenticated )    
    serializer_class = regserialzer
    
    def post(self, request):
        try:
            ser = regserialzer(data=request.data)
            ser.is_valid()
            ser.save()
            print(returnresponse(data=ser.data,status_code=200,message="Success",))
            return Response(ser.data)
        except : 
            return Response("error occuer")
    def get(self,request):
        try:
            
            user  = Account.objects.all()
            x = returnresponse(data=user,status_code=200,message="Success",)
            x = [x,]
            return Response({'data':x})
        except:
            return Response({
                "Result":"Somethinging went wrong"
            })

class UserUpdate(generics.GenericAPIView):
    serializer_class =regserialzer
    queryset = Account.objects.all()
    permission_classes = (IsAdminUser, )

    def get(self, request,id):
        user = Account.objects.get(id=id)
        return Response(data={"message": regserialzer(user).data}, status=status.HTTP_201_CREATED)
    
    def put(request,self,id):
       user = Account.objects.get(id=id)
       print(user.email)
       return Response(user)

class SuperUser(generics.CreateAPIView):
    
    serializer_class = SuperAdminserializer
    query_set = User.objects.all()
    def post(self, request):
        try:
           user = User()
           user.email= request.data.get('email')
           user.username= request.data.get('username')
           user.password= make_password(request.data.get('password'))
           user.first_name= request.data.get('first_name')
           user.last_name   = request.data.get('last_name')
           user.save()
           return Response({"result":SuperAdminserializer(user).data})
        except Exception as e: 
            response = json.loads('{"message":e}')
            return response

    def get(self,request):
        try:
            user  = User.objects.all()
            ser = SuperAdminserializer(data=user,many=True)
            ser.is_valid()
            # print(ser)
            return Response({"result":ser.data})
        except:
            return Response({
                "Result":"Somethinging went wrong"
            })
            
        
   