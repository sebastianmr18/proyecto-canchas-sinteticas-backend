from rest_framework import viewsets
from ..models.user_model import User
from ..models.court_model import Court
from ..models.reservation_model import Reservation
from ..models.review_model import Review
from ..models.payment_model import Payment
from ..serializers.serializers import CourtSerializer, ReservationSerializer, PaymentSerializer, ReviewSerializer



class CourtViewSet(viewsets.ModelViewSet):
    queryset = Court.objects.all()
    serializer_class = CourtSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
