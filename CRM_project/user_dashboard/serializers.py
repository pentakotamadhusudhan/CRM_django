from rest_framework import serializers
from .models import Account
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import make_password, check_password



class regserialzer(serializers.ModelSerializer):
    class Meta:
        model  = Account
        fields = "__all__"
        
        def create(self, validated_data):
            print("-------------------------------------------","re_enter")
            print(make_password(validated_data['password']))
            user = Account.objects.create_user(name=validated_data['name'], email=validated_data['email'],
                                            password= make_password(validated_data["password"]),
                                            role=validated_data['role'])
            
            return user


class SuperAdminserializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields =('username', 'email', 'password','first_name','last_name')
        extra_kwargs = {'password': {'write_only': True}}
       
        