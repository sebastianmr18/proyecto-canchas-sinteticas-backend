from rest_framework import serializers
from ..models.court_model import Court
from ..models.reservation_model import Reservation
from ..models.review_model import Review
from ..models.payment_model import Payment


class CourtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Court
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
