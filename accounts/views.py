from backend.models import *
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .serializers import *

from rest_framework.response import Response
from django.db.models import Q
from rest_framework.views import APIView

from rest_framework import status

class CustomerRegister(APIView):
    def post(self, req):
        serialize = CustomerCreateSerializer(data=req.data)
        if serialize.is_valid():
            serialize.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_208_ALREADY_REPORTED)



class WorkerRegister(APIView):
    def post(self, req):
        serialize = WorkerCreateSerializer(data=req.data)
        if serialize.is_valid():
            serialize.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_208_ALREADY_REPORTED)