from rest_framework import serializers
from backend.models import *
from django.contrib.auth.models import User

class CustomerCreateSerializer(serializers.ModelSerializer):
    class UserModelSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ['first_name', 'last_name', 'username', 'password' ]

    user = UserModelSerializer()

    class Meta:
        model = Customer
        fields = '__all__'

    def create(self, validated_data):
        us = validated_data['user']
        # breakpoint()

        user = User.objects.create(
            username=us['username'],
            first_name=us['first_name'],
            last_name=us['last_name']
        )

        user.set_password(us['password'])
        user.save()

        
        mobile = validated_data['mobile']
        address = validated_data['address']  

        user = Customer.objects.create(mobile=mobile, address=address, user=user)
        user.save()
        return user