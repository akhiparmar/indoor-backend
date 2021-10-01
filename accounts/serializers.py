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
        




class WorkerCreateSerializer(serializers.ModelSerializer):
    class UserModelSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ['first_name', 'last_name', 'username', 'password' ]

    user = UserModelSerializer()

    class Meta:
        model = Worker
        fields = '__all__'

    def create(self, validated_data):
        us = validated_data['user']
        # breakpoint()

        user = User.objects.create(
            username=us['username'],
            first_name=us['first_name'],
            last_name=us['last_name']
        )
        #id,user,image,mobile,pincode,address

        user.set_password(us['password'])
        user.save()


        mobile = validated_data['mobile']
        pincode = validated_data['pincode']
        address = validated_data['address']  

        user = Worker.objects.create(user=user, mobile=mobile, pincode=pincode, address=address)
        user.save()
        return user