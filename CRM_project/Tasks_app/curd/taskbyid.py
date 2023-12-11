from rest_framework import generics
from rest_framework.response import Response
from GenericResponse import returnresponse
from ..serializers import *
from ..models import TaskModels

class TaskById(generics.UpdateAPIView):
    serializer_class = task_serializer
    queryset = TaskModels.objects.all()
    lookup_field = 'id'

    # def put(self, request,id):
    #     try:

    #         ser = task_serializer(instance=request.data)
    #         ser.is_valid()
    #         ser.save()
    #         print(ser.data)
    #         response = returnresponse(status_code=200,data=ser.data,message='Success')
    #         return Response(response)
    #     except : 
    #         return Response("error occuer")
        