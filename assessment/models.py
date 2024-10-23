from django.db import models
from accounts.models import User
from django.template.defaultfilters import slugify

    
class UserAssessmentData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    health_goal = models.CharField(max_length=250)
    gender = models.CharField(max_length=15)
    age = models.PositiveIntegerField() 
    weight = models.PositiveIntegerField()
    mood = models.IntegerField()
    is_professional_help = models.IntegerField()
    is_physical_distress = models.IntegerField()
    sleep_quality = models.IntegerField()
    medications = models.IntegerField()
    other_mental_symptom = models.TextField()
    stress_level = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.email} - {self.health_goal}"
    

    def calculate_mental_score(self):
        score_list = [int(self.mood), self.is_physical_distress, self.is_professional_help, self.sleep_quality, self.medications, self.stress_level]
        total_score = sum(score_list)
        max_score = 23
        
        mental_score = (total_score / max_score) * 100
        return round(mental_score, 2)