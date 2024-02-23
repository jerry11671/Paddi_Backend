from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import HealthGoalAPIView, AssessmentCreateAPIView, AssessmentGetAPIView

router = DefaultRouter()
router.register(r'health_goals', HealthGoalAPIView)


urlpatterns = [
    path('', include(router.urls)),
    path('assessment_create/', AssessmentCreateAPIView.as_view()),
    path('assessment_list/', AssessmentGetAPIView.as_view()),
]