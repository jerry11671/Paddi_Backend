from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AssessmentCreateAPIView, AssessmentGetAPIView


urlpatterns = [
    path('assessment_create/', AssessmentCreateAPIView.as_view()),
    path('assessment_list/', AssessmentGetAPIView.as_view()),
]
