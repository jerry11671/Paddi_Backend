from rest_framework import serializers

from .models import Assessment

class AssessmentSerializer(serializers.ModelSerializer):
    mental_score = serializers.SerializerMethodField()
    class Meta:
        model = Assessment
        exclude = ['user']

    def get_mental_score(self, obj):
        return obj.calculate_mental_score()

