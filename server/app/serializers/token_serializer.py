from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    user = serializers.SerializerMethodField()


    def get_user(self, obj):
        user = obj.user
        return {
            'user_id': user.user_id,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        }
    
    def validate(self, attrs):
        data = super().validate(attrs)
        data['user'] = self.get_user(self)  # Añadir la información del usuario al token
        return data    