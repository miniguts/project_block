from django.urls import path, include

from api.views import ArticleList, ArticleDetail

urlpatterns = [
    path('articles/', ArticleList.as_view()),
    path('article/<int:pk>', ArticleDetail.as_view()),
]