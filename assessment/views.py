from django.shortcuts import render

from rest_framework import generics, viewsets, views
from rest_framework import permissions
from rest_framework.response import Response

from .serializers import AssessmentSerializer
from .models import  Assessment


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


