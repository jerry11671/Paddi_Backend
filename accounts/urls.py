from django.urls import path 
from .views import LoginView, LogoutView, UserRegistrationView, GetAllUsers, UpdateProfileView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('users', GetAllUsers.as_view()),
    path('signup', UserRegistrationView.as_view(), name='signup'),

    path('login', LoginView.as_view(), name='login'),
    path('auth/get_token/', TokenObtainPairView.as_view(), name='login'),
    path('auth/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('update_profile', UpdateProfileView.as_view()),
]
