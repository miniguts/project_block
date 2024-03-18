from rest_framework import mixins, generics, permissions
from rest_framework.viewsets import GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from article.models import Article
from article.serializers import ArticleSerializer
from authorization.models import User
from authorization.serializers import UserProfileSerializer


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArtcileDetail(generics.RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAdminUser]


class ArticleView(GenericViewSet, mixins.ListModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields =  ['title', 'created_at']
    search_filters = ['author',]
    ordering_fields = ['title',]
    ordering = ['created_at']


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAdminUser]

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAdminUser]

class UserView(GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer