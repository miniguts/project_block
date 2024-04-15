from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api.views import (ArticleView, CommentView, get_location, GroupView)


router = DefaultRouter()
router.register('articles', ArticleView, basename='Articles')
router.register('comment', CommentView, basename='Comment')
router.register('group', GroupView, basename='Group')

urlpatterns = [
    path('article_view_set/', include(router.urls)),
    path('get_location/', get_location, name='get_location')
]