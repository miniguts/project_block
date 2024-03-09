from django.urls import path, include

from article.views import (
    article_list, 
    article_detail, 
    article_new, 
    article_edit
)

urlpatterns = [
    path('', article_list, name='article_list'),
    path('<int:pk>/detail/',article_detail, name='article_detail'),
    path('<int:pk>/edit/',article_edit ,name = 'article_edit'),
    path('new/',article_new,name='article_new'),
]
