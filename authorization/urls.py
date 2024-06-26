from django.urls import path, include

from authorization.views import (
    TokenObtainPairView,
    TokenRefreshView,
    UserRegisterView,
    UserProfileView,
    UserProfileEditView,
    UserProfileDeletView
)

urlpatterns = [
    path('token/',TokenObtainPairView.as_view()),
    path('token/refresh/',TokenRefreshView.as_view()),
    path('register/', UserRegisterView.as_view()),
    path('profile/', UserProfileView.as_view()),
    path('name_change/', UserProfileEditView.as_view()),
    path('delete_profile/', UserProfileDeletView.as_view({'delete': 'delete_profile'}))
]
