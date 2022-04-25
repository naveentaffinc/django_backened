from rest_framework import serializers
from .models import CustomUserModel


class CustomUserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(max_length = 100)
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length = 100)

    class Meta:
        model = CustomUserModel
        fields = ('__all__')
