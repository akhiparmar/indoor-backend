
from .models import *
from rest_framework.generics import ListAPIView
from .worker_serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import datetime


from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser






class MyBookings(ListAPIView):
    serializer_class = BookingSerializer
    

    def get_queryset(self):
        try:
            worker = Worker.objects.get(user__id = self.request.user.id)
            return Booking.objects.filter(worker=worker).order_by('booking_date').reverse()
        except:
            return {}

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]




class Profile(APIView):
    parser_classes = (MultiPartParser, FormParser, FileUploadParser,)

    def get(self, req):
        serialize = WorkerProfileSerializer(Worker.objects.get(user__id=self.request.user.id))
        return Response(serialize.data)


    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]






class BookCustomer(APIView):
    def post(self, request, pk, formar=None):
        try:
            # breakpoint()
            worker = Worker.objects.get(user__id=self.request.user.id)
            book = Booking.objects.filter(id=pk,worker=worker)
            book.update(accepted=True, acceptance_date=datetime.datetime.now())
            return Response({}, status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
