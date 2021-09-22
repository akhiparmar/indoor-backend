
from .models import *
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .serializers import *
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.views import APIView



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
        # if Service.objects.get(name=service):
        #         service_id = Service.objects.get(name=service).id
        #         return Profession.objects.filter(service__id=service_id, worker__pincode = pincode)
        # else:
        #     return Profession.objects.all()

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
        # if Service.objects.get(name=service):
        #         service_id = Service.objects.get(name=service).id
        #         return Profession.objects.filter(service__id=service_id, worker__pincode = pincode)
        # else:
        #     return Profession.objects.all()






class WorkerReviews(ListAPIView):
    serializer_class = WorkerReviewSerializer

    def get_queryset(self):
        id = self.kwargs['pk']

        try:
            return Review.objects.filter(worker__user__id=id)
        except:
            return {}
        # if Service.objects.get(name=service):
        #         service_id = Service.objects.get(name=service).id
        #         return Profession.objects.filter(service__id=service_id, worker__pincode = pincode)
        # else:
        #     return Profession.objects.all()

    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]