from rest_framework import serializers
from ..models.court_model import Court, CourtImage
from ..models.reservation_model import Reservation
from ..models.review_model import Review
from ..models.payment_model import Payment
from ..models.coupon_model import Coupon
from ..models.notification_model import Notification
from ..models.reservation_history_model import ReservationHistory
from datetime import timedelta


class CourtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Court
        fields = '__all__'

class CourtImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourtImage
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

    def validate(self, data):
        court = data['court']
        start_datetime = data['start_datetime']
        duration_hours = data['duration_hours']        
        duration_minutes = duration_hours * 60 - 1

        end_datetime = start_datetime + timedelta(minutes=duration_minutes)        

        overlapping_reservations = Reservation.objects.filter(
            court=court,
            start_datetime__lt=end_datetime,
            start_datetime__gte=start_datetime - timedelta(minutes=duration_minutes),
        )        
        if overlapping_reservations.exists():        
            raise serializers.ValidationError('La reserva se solapa con otra reserva anterior.')
        
        return data        

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class ReservationHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationHistory
        fields = '__all__'