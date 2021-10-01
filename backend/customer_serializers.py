from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class WorkerCardSerializer(serializers.ModelSerializer):
    class Worker(serializers.ModelSerializer):
        class UserModelSerializer(serializers.ModelSerializer):
            class Meta:
                model = User
                fields = ['first_name', 'last_name']

        user = UserModelSerializer()

        class Meta:
            model = Worker
            fields = ['id', 'user', 'rating', 'mobile', 'pincode']


    worker = Worker()
    # service = Service(many=True)

    class Meta:
        model = Profession
        fields = ['worker']




#This is Serializer for Worker profile
class WorkerProfileSerializer(serializers.ModelSerializer):
    class Worker(serializers.ModelSerializer):
        class UserModelSerializer(serializers.ModelSerializer):
            class Meta:
                model = User
                fields = ['first_name', 'last_name']

        user = UserModelSerializer()
        class Meta:
            model = Worker
            fields = ['id', 'user', 'rating', 'mobile', 'pincode', 'address']

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
                fields = ['first_name', 'last_name']

        user = UserModelSerializer()
        class Meta:
            model = Customer
            fields = ['user']

    customer = Customer()
    class Meta:
        model = Review
        fields = ['customer', 'rating', 'date', 'feedback']



class WorkerReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['worker', 'rating', 'feedback']

    def create(self, validated_data, **kwargs):
        worker_id = validated_data['worker']
        rating = validated_data['rating']
        feedback = validated_data['feedback']
        worker = Worker.objects.get(id=worker_id)
        customer = kwargs['customer']
        customer = Customer.objects.get(id=customer)
        review = Review.objects.create(customer=customer, worker=worker, rating=rating, feedback=feedback)
        return review



class BookWorkerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Booking
        fields = ['worker']

    def create(self, validated_data, **kwargs):
        worker = validated_data['worker']
        worker = Worker.objects.get(id=worker)
        customer = kwargs['customer']
        customer = Customer.objects.get(id=customer)
        book = Booking.objects.create(customer=customer, worker=worker)
        return book



class CustomerProfileSerializer(serializers.ModelSerializer):
    class UserModelSerializer(serializers.ModelSerializer):
            class Meta:
                model = User
                fields = ['id', 'first_name', 'last_name', 'username']

    user = UserModelSerializer()

    class Meta:
        model = Customer
        fields = '__all__'


#This is Serializer for all Booking Records
class BookingSerializer(serializers.ModelSerializer):
    class WorkerProfileSerializer(serializers.ModelSerializer,):
        class UserModelSerializer(serializers.ModelSerializer):
            class Meta:
                model = User
                fields = ['first_name', 'last_name']

        user = UserModelSerializer()

        class Meta:
            model = Worker
            fields = ['id', 'user']

    worker = WorkerProfileSerializer()

    class Meta:
        model = Booking
        exclude = ['id', 'customer']