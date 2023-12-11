from rest_framework import generics
from rest_framework.response import Response
from GenericResponse import returnresponse
from ..serializers import *

class CreateTasks(generics.GenericAPIView):
    # permission_classes = (IsAuthenticated, )    
    serializer_class =task_serializer

    def post(self, request):
        try:
            ser = task_serializer(data=request.data)
            ser.is_valid()
            ser.save()
            response = returnresponse(status_code=200,data=ser.data,message="success")
            return Response(response)
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
  
    