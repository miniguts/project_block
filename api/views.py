from django.shortcuts import render,get_object_or_404
from article.models import Article
from article.serializers import ArticleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from authorization.permissions import IsSuperAdmin


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.AllowAny]
    

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]
    #permission_classes = [permissions.IsAuthenticated, IsSuperAdmin | IsCourier]
    #permission_classes = [permissions.IsAuthenticated, IsSuperAdmin & IsCourier]