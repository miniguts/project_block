from django.urls import path, include

from article.views import article_list



urlpatterns = [
    path('', article_list, name='article_list')
]