from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)
import requests


from article.models import Comment, Article, Group_up
from article.serializers import CommentSerializer, ArticleSerializer, GroupSerializer



class ArticleView(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                   mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticated, ]
    filterset_fields =  ['created_at']
    search_fields = ['title', 'description']
    ordering = ['-id', '-created_at']

    def create_article(self, request, *args, **kwargs):
        article = Article.objects.create(
        author= request.user,
        title=request.data['title'], 
        type_content=request.data['type_content'],
        )
        serializer = ArticleSerializer(article)
        return Response(data=serializer.data)


class CommentView(GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [OrderingFilter, DjangoFilterBackend, SearchFilter]
    filterset_fields = ['created_at',]
    permission_classes = [IsAuthenticated,]

    def create_comment(self, request, *args, **kwargs):
        article = get_object_or_404(Article.objects.all(), pk=request.data['post'])
        comment = Comment.objects.create(
            post = article,
            body = request.data['body'],
            author = request.user
            )
        serializer = CommentSerializer(comment)
        return Response(data=serializer.data)


class GroupView(GenericViewSet, mixins.ListModelMixin ,mixins.CreateModelMixin, mixins.DestroyModelMixin):
    queryset = Group_up.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated,]


@api_view(['GET'])
def get_location(request):
    url = "http://ipwho.is/"

    headers = {}
    payload = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()

    country = data['country']
    city = data['city']

    return Response({'country': country, 'city': city})