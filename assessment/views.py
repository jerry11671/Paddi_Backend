from django.shortcuts import render

from rest_framework import generics, viewsets, views
from rest_framework import permissions
from rest_framework.response import Response

from .serializers import HealthGoalSerializer, AssessmentSerializer
from .models import HealthGoal, Assessment



class HealthGoalAPIView(viewsets.ModelViewSet):
    serializer_class  = HealthGoalSerializer
    queryset = HealthGoal.objects.all()
    permission_classes = [permissions.IsAdminUser]


class AssessmentCreateAPIView(generics.CreateAPIView):
    serializer_class = AssessmentSerializer
    queryset = Assessment
    permission_classes = [permissions.IsAuthenticated]

#   we don't have to show the user here, the user is the person that is authenticated.
    def perform_create(self, serializer):
        assessment = serializer.save(user=self.request.user)
        assessment.calculate_mental_score()
        assessment.save()


class AssessmentGetAPIView(generics.ListAPIView):
    serializer_class = AssessmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = Assessment.objects.filter(user=self.request.user.id)
        return qs      


