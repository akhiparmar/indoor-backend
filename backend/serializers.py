from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


#This is SHOW WorkerCard deitail
class WorkerCardSerializer(serializers.ModelSerializer):
    class Worker(serializers.ModelSerializer):
        class UserModelSerializer(serializers.ModelSerializer):
            class Meta:
                model = User
                fields = ['id', 'username', 'first_name', 'last_name']

        user = UserModelSerializer()
        class Meta:
            model = Worker
            fields = '__all__'

    class Service(serializers.ModelSerializer):
        class Meta:
            model = Service
            fields = ['name']

    worker = Worker()
    # service = Service(many=True)

    class Meta:
        model = Profession
        fields = ['id','worker']




#This is Serializer for Worker profile
class WorkerProfileSerializer(serializers.ModelSerializer,):
    class Worker(serializers.ModelSerializer):
        class UserModelSerializer(serializers.ModelSerializer):
            class Meta:
                model = User
                fields = ['id', 'username', 'first_name', 'last_name']

        user = UserModelSerializer()
        class Meta:
            model = Worker
            fields = '__all__'

    class Service(serializers.ModelSerializer):
        class Meta:
            model = Service
            fields = ['name']

    worker = Worker()
    service = Service(many=True)

    class Meta:
        # model = Worker
        model = Profession
        fields = '__all__'