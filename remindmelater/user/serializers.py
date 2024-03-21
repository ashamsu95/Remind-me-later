from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserDetail

class UserRegistrationSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(max_length=15, allow_blank=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'phone_number']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        phone_number_data = validated_data.pop('phone_number', None)
        user = User.objects.create_user(**validated_data)
        if phone_number_data:
            UserDetail.objects.create(user=user, phone_number=phone_number_data)
        return user
