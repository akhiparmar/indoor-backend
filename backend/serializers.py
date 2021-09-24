from django.db.models import fields
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.fields import CurrentUserDefault


#This is SHOW WorkerCard deitail
class WorkerCardSerializer(serializers.ModelSerializer):
    class Worker(serializers.ModelSerializer):
        class UserModelSerializer(serializers.ModelSerializer):
            class Meta:
                model = User
                fields = ['id', 'first_name', 'last_name']

        user = UserModelSerializer()

        class Meta:
            model = Worker
            fields = ['id', 'user', 'image', 'rating', 'mobile', 'pincode']


    worker = Worker()
    # service = Service(many=True)

    class Meta:
        model = Profession
        fields = ['worker']




#This is Serializer for Worker profile
class WorkerProfileSerializer(serializers.ModelSerializer,):
    class Worker(serializers.ModelSerializer):
        class UserModelSerializer(serializers.ModelSerializer):
            class Meta:
                model = User
                fields = ['id', 'first_name', 'last_name']

        user = UserModelSerializer()
        class Meta:
            model = Worker
            fields = ['id', 'user', 'image', 'rating', 'mobile', 'pincode', 'address']

    class Service(serializers.ModelSerializer):
        class Meta:
            model = Service
            fields = ['name']

    worker = Worker()
    service = Service(many=True)

    class Meta:
        # model = Worker
        model = Profession
        fields = ['worker', 'service']






class WorkerReviewSerializer(serializers.ModelSerializer):
    class Customer(serializers.ModelSerializer):
        class UserModelSerializer(serializers.ModelSerializer):
            class Meta:
                model = User
                fields = ['id', 'first_name', 'last_name']

        user = UserModelSerializer()
        class Meta:
            model = Customer
            fields = ['user']

    customer = Customer()
    class Meta:
        model = Review
        fields = ['customer', 'rating', 'date', 'feedback']



class BookWorkerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Booking
        fields = '__all__'



class CustomerProfileSerializer(serializers.ModelSerializer):
    class UserModelSerializer(serializers.ModelSerializer):
            class Meta:
                model = User
                fields = ['id', 'first_name', 'last_name']

    user = UserModelSerializer()

    class Meta:
        model = Customer
        fields = '__all__'