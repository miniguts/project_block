from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from article.views import article_list



urlpatterns = [
    path('', article_list, name='article_list')
]
