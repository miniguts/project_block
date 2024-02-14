from django.urls import path, include

from users.views import user_list



urlpatterns = [
    path('', user_list, name='user_list')
]