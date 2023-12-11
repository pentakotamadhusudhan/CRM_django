from .models import *
from rest_framework import serializers

class task_serializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModels
        fields  = "__all__"

class update_task_serializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = TaskModels
        fields  = ['task_name','task_description','assign_to','id']

        # def create(self,request):
