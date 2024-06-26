from django.shortcuts import render
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from authorization.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework import generics
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)
from authorization.serializers import (
    TokenObtainPairSerializer, 
    TokenRefreshSerializer,
    UserProfileSerializer,
    UserNameEditSerializer
)

class TokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = TokenObtainPairSerializer


class TokenRefreshView(TokenRefreshView):
    permission_classes = [AllowAny]
    serializer_class = TokenRefreshSerializer


'''{
    "username":"Vadim",
    "password":"1234",
    "first_name":"vadim",
    "email":"ema@mail.kz",
    "role":2
}'''

class UserRegisterView(APIView):

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        first_name = request.data['first_name']
        email = request.data['email']
        role = request.data['role']
        try:
            get_object_or_404(User.objects.all(), username=username)
            return Response(data={'info':'Пользователь уже существует'},status=status.HTTP_409_CONFLICT)
        except:
            User.objects.create(
                username=username, 
                password=make_password(password),
                first_name=first_name,
                email=email,
                role=role)
            return Response(status=status.HTTP_200_OK)
        

class UserProfileView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = UserProfileSerializer

    def get(self, request):
        user = request.user
        serializer = UserProfileSerializer(user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    


class UserProfileEditView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = UserNameEditSerializer

    def post(self, request):
        first_name = request.data['first_name']
        user = request.user
        user.first_name=first_name
        user.save()
        return Response(status=status.HTTP_200_OK)
    

class UserProfileDeletView(GenericViewSet):
    permission_classes = [IsAuthenticated]

    def delete_profile(self, request):
        user = request.user
        user.delete()
        return Response(data={'info':'Пользователь был удален'},status=status.HTTP_204_NO_CONTENT)