from rest_framework import viewsets
from ..models.user_model import User
from ..models.court_model import Court, CourtImage
from ..models.reservation_model import Reservation
from ..models.review_model import Review
from ..models.payment_model import Payment
from ..models.coupon_model import Coupon
from ..models.notification_model import Notification
from ..models.reservation_history_model import ReservationHistory
from ..serializers.serializers import CourtSerializer, CourtImageSerializer, ReservationSerializer, PaymentSerializer, ReviewSerializer, NotificationSerializer, ReservationHistorySerializer, CouponSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import timedelta
from rest_framework.exceptions import ValidationError


class CourtViewSet(viewsets.ModelViewSet):
    queryset = Court.objects.all()
    serializer_class = CourtSerializer

class CourtImageViewSet(viewsets.ModelViewSet):
    queryset = CourtImage.objects.all()
    serializer_class = CourtImageSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def create(self, request, *args, **kwargs):        
        data = request.data        

        payment_method = data.get('payment_method')        
        
        if payment_method == 'efectivo':
            data['payment_status'] = 'Pendiente'
        
        elif payment_method == 'tarjeta':
            data['payment_status'] = 'Exitoso'
            data['is_confirmed'] = True

        # Serializar y guardar
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Retornar la respuesta
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class ReservationHistoryViewSet(viewsets.ModelViewSet):
    queryset = ReservationHistory.objects.all()
    serializer_class = ReservationHistorySerializer

class CouponViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
