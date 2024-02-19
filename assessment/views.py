from django.shortcuts import render

from rest_framework import generics, viewsets
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response

from .serializers import HealthGoalSerializer, AssessmentSerializer
from .models import HealthGoal, Assessment
# from .permissions import IsAdminOrReadOnly



class HealthGoalAPIView(viewsets.ModelViewSet):
    serializer_class  = HealthGoalSerializer
    queryset = HealthGoal.objects.all()
    permission_classes = [permissions.IsAdminUser]

    # def get_superuser(self):
    #     user = self.request.user
    #     if user.is_authenticated and user.is_superuser:
    #         return user
    #     else:
    #         raise ValueError("This user is not a superuser")

    # def perform_create(self, serializer):
    #     user = self.get_superuser()
    #     serializer.save(user=user)

class AssessmentCreateAPIView(generics.CreateAPIView):
    serializer_class = AssessmentSerializer
    queryset = Assessment.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class AssessmentGetAPIView(generics.ListAPIView):
    serializer_class = AssessmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        health_goal = HealthGoal.objects.get(slug=slug, user=self.request.user.id)
        qs = Assessment.objects.filter(health_goal=health_goal)
        return qs

        


