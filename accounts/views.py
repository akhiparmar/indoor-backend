from backend.models import *
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .serializers import *

from rest_framework.response import Response
from django.db.models import Q
from rest_framework.views import APIView

class CustomerRegister(APIView):
    def post(self, req):
        serialize = CustomerCreateSerializer(data=req.data)
        if serialize.is_valid():
            serialize.save()
            return Response({"message":"data saved"})
        return Response(serialize.errors)