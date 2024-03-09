from django.shortcuts import render,get_object_or_404
from article.models import Article
from article.serializers import ArticleSerializer
from authorization.models import User
from authorization.serializers import UserProfileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from authorization.permissions import IsSuperAdmin


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # permission_classes = [permissions.AllowAny]
    

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]
    #permission_classes = [permissions.IsAuthenticated, IsSuperAdmin | IsCourier]
    #permission_classes = [permissions.IsAuthenticated, IsSuperAdmin & IsCourier]


class ArticleView(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAdminUser]


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAdminUser]

class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer