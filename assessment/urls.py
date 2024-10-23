from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AssessmentCreateAPIView, GetAssessmentAPIView


urlpatterns = [
    path('create', AssessmentCreateAPIView.as_view()),
    path('', GetAssessmentAPIView.as_view()),
]
