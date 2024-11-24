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
