from rest_framework import mixins, generics, permissions
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from article.models import Article
from article.serializers import ArticleSerializer
from authorization.models import User
from authorization.serializers import UserProfileSerializer


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer()

class ArtcileDetail(generics.RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer()
    permission_classes = [permissions.IsAdminUser]


class ArticleView(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer()
    permission_classes = [permissions.IsAdminUser]

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer()
    permission_classes = [permissions.IsAdminUser]

class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer()