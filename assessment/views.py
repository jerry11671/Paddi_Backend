from django.shortcuts import render

from rest_framework import generics, status
from rest_framework import permissions
from rest_framework.response import Response

from .serializers import AssessmentSerializer
from .models import  UserAssessmentData


class AssessmentCreateAPIView(generics.GenericAPIView):
    serializer_class = AssessmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        queryset = UserAssessmentData.objects.all()
        data = request.data
        user = request.user

        serializer = self.serializer_class(queryset, data=data)
        if serializer.is_valid():
            user_assessment_data = UserAssessmentData.objects.create(user=user, **serializer.validated_data)
            return Response({'status': True, 'msg': 'Your assessment data have been saved'}, status=status.HTTP_200_OK)
        return Response({'status': False, 'msg': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



class GetAssessmentAPIView(generics.ListAPIView):
    serializer_class = AssessmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = UserAssessmentData.objects.get(user=self.request.user)
        return qs   

    def get(self, request):
        serializer = self.serializer_class(self.get_queryset())
        return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)
           


