
from rest_framework.response import Response
from rest_framework import status,viewsets
from .serializers import CustomUserSerializer
from .models import CustomUserModel
from django.contrib.auth.hashers import make_password,check_password
from rest_framework.views import APIView


class CustomUserViewSets(viewsets.ModelViewSet):

    queryset = CustomUserModel.objects.all()
    serializer_class = CustomUserSerializer

    # Hashing the password using the make_password() inbuilt function 

    def create(self, request, *args, **kwargs):
        user = request.data
        newUser = CustomUserModel.objects.create(username = user['username'], email= user['email'], password = make_password(user['password']))
        newUser.save()

        serializer = CustomUserSerializer(newUser)

        return Response(serializer.data)

    def checkPassword(self, request, *args, **kwargs):

        """
        Function that gets the username and password from the requests and validates it and response.
        """
        
        user = self.queryset.filter(username = request.data['username'])

        validate = check_password(request.data['password'], user[0].password)

        
        return Response({"message": validate})

        

