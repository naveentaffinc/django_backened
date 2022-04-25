from rest_framework import serializers
from .models import CustomUserModel


class CustomUserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(max_length = 100)
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length = 100)

    class Meta:
        model = CustomUserModel
        fields = ('__all__')

    # def create(self, validated_data):
    #    user = CustomUserModel()
    #    user.username = validated_data['username']
    #    user.email = validated_data['email']
    #    user.Password = make_password(validated_data['password'])

    #    return user