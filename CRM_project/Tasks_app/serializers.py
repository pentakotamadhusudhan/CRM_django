from .models import *
from rest_framework import serializers

class task_serializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModels
        fields  = "__all__"