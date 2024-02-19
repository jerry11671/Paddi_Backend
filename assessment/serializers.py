from rest_framework import serializers

from .models import HealthGoal, Assessment

class HealthGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthGoal
        fields = ['id', 'user', 'health_goal', 'slug']


class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = "__all__"

    # def save(self, data):
    #     user = self.request.user
    #     qs = 
    #     health_goal = data['health_goal']

