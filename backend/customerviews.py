
from .models import *
from rest_framework.generics import ListAPIView
from .customer_serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status



from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication


class Workers(ListAPIView):
    serializer_class = WorkerCardSerializer

    def get_queryset(self):
        service = self.request.GET.get('service')
        pincode = self.request.GET.get('pincode')

        try:
            service_id = Service.objects.get(name=service).id
            return Profession.objects.filter(service__id=service_id, worker__pincode = pincode).order_by('worker__rating').reverse()
        except:
            return {}

    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]



class WorkerProfile(ListAPIView):
    serializer_class = WorkerProfileSerializer

    def get_queryset(self):
        id = self.kwargs['pk']

        try:
            return Profession.objects.filter(worker__id=id)
        except:
            return {}

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]



class WorkerReviews(APIView):
    def get(self, request, pk, format=None):
        try:
            reviews = Review.objects.filter(worker__id=pk).order_by('date').reverse()
            serialize = WorkerReviewSerializer(reviews, many=True)
            return Response(serialize.data, status=status.HTTP_200_OK)
        except:
            return Response({"message":"Not found"}, status=status.HTTP_204_NO_CONTENT)


    def post(self, request, pk=None, format=None):
        serialize = WorkerReviewCreateSerializer(data=self.request.data)
        if serialize.is_valid():
            serialize.create(validated_data=request.data,customer=Customer.objects.get(user__id=self.request.user.id).id)
            try:
                initial_data = serialize.initial_data
                worker = Worker.objects.get(id=initial_data['worker'])
                prev_rating = worker.rating
                rating = (prev_rating+int(initial_data['rating']))
                new_rating = rating//2
                Worker.objects.filter(id=worker.id).update(rating=new_rating)
            except:
                pass

            return Response({}, status=status.HTTP_201_CREATED)
        return Response(serialize.errors)


    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


# class BookWorker(CreateAPIView):
#     queryset = Booking.objects.all()
#     serializer_class = BookWorkerSerializer

#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]

class BookWorker(APIView):
    def post(self, request):
        serialize = BookWorkerSerializer(data=request.data)
        if serialize.is_valid():
            serialize.create(validated_data=request.data,customer=Customer.objects.get(user__id=self.request.user.id).id)
            return Response({}, status=status.HTTP_201_CREATED)
        return Response(serialize.errors)

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]



class Profile(APIView):

    def get(self, req):
        serialize = CustomerProfileSerializer(Customer.objects.get(user__id=self.request.user.id))
        return Response(serialize.data)

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
        


class MyBookings(ListAPIView):
    serializer_class = BookingSerializer
    

    def get_queryset(self):
        try:
            customer = Customer.objects.get(user__id = self.request.user.id)
            return Booking.objects.filter(customer=customer).order_by('booking_date').reverse()
        except:
            return {}

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]