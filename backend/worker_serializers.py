from django.db.models import fields
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User






#This is Serializer for all Booking Records
class BookingSerializer(serializers.ModelSerializer):
    class CustomerProfileSerializer(serializers.ModelSerializer):
        class UserModelSerializer(serializers.ModelSerializer):
            class Meta:
                model = User
                fields = ['first_name', 'last_name']

        user = UserModelSerializer()

        class Meta:
            model = Customer
            exclude = ['id']

    customer = CustomerProfileSerializer()

    class Meta:
        model = Booking
        exclude = ['worker']



class WorkerProfileSerializer(serializers.ModelSerializer):
    class UserModelSerializer(serializers.ModelSerializer):
            class Meta:
                model = User
                fields = ['first_name', 'last_name', 'username']

    user = UserModelSerializer()

    class Meta:
        model = Worker
        fields = '__all__'



class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = "__all__"
        # fields = ['worker', 'service']