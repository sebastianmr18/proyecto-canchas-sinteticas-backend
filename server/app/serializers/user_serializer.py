from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from ..models.user_model import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['user_id','email', 'first_name', 'last_name', 'password', 'confirm_password']
        
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Las contraseñas no coinciden."})

        return attrs

    def create(self, validated_data):
        user = User(
            user_id=validated_data['user_id'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
