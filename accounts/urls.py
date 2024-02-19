from django.urls import path 
from .views import LoginView, LogoutView, UserRegistrationView, GetAllUsers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('all_users/', GetAllUsers.as_view()),
    path('auth/signup/', UserRegistrationView.as_view(), name='user-signup'),

    # path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('auth/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('auth/logout/', LogoutView.as_view(), name='logout'),
]
