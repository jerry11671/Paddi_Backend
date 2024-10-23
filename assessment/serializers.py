from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import UserAssessmentData

class AssessmentSerializer(serializers.ModelSerializer):
    mental_score = serializers.SerializerMethodField()
    class Meta:
        model = UserAssessmentData
        exclude = ['user']

    def validate(self, obj):
        if obj == "":
            raise ValidationError({'msg': 'This field must not be empty'})
        return obj

    def get_mental_score(self, obj):
        return obj.calculate_mental_score()
        
        
    