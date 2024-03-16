from django.urls import path, include

from rest_framework.routers import DefaultRouter

# from api.views import ArticleList
from api.views import  ArticleView, UserView


router = DefaultRouter()
router.register('articles', ArticleView, basename='articles')
router.register('user', UserView, basename='user')

urlpatterns = [
    path('article_view_set/', include(router.urls)),
]