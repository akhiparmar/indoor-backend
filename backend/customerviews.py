
from .models import *
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .serializers import *
from rest_framework.response import Response
from django.db.models import Q, query
from rest_framework.views import APIView


from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication


class Workers(ListAPIView):
    serializer_class = WorkerCardSerializer

    def get_queryset(self):
        service = self.request.GET.get('service')
        pincode = self.request.GET.get('pincode')

        try:
            service_id = Service.objects.get(name=service).id
            return Profession.objects.filter(service__id=service_id, worker__pincode = pincode)
        except:
            return {}

    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]



class WorkerProfile(ListAPIView):
    # queryset = Profession.objects.all()
    serializer_class = WorkerProfileSerializer

    def get_queryset(self):
        id = self.kwargs['pk']

        try:
            return Profession.objects.filter(worker__user__id=id)
        except:
            return {}






class WorkerReviews(ListAPIView):
    serializer_class = WorkerReviewSerializer

    def get_queryset(self):
        id = self.kwargs['pk']

        try:
            return Review.objects.filter(worker__user__id=id)
        except:
            return {}

    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]


class BookWorker(CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookWorkerSerializer



class Profile(APIView):

    def get(self, req):
        serialize = CustomerProfileSerializer(Customer.objects.get(user__id=self.request.user.id))
        return Response(serialize.data)
    # queryset = Customer.objects.all()
    # serializer_class = CustomerProfileSerializer
    
    # def get_queryset(self):
    #     return Customer.objects.get(user__id=self.request.user.id)

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
        