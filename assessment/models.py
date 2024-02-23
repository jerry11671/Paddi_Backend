from django.db import models
from accounts.models import User
from django.template.defaultfilters import slugify
from .utils import min_max_validator

    
class Assessment(models.Model):
    
    HEALTH_GOAL_CHOICES = (
    ('I wanna reduce stress', 'I wanna reduce stress'),
    ('I wanna try AI Therapy', 'I wanna try AI Therapy'),
    ('I want to cope with trauma', 'I want to cope with trauma'),
    ('I want to be a better person', 'I want to be a better person'),
    ('Just trying out the website', 'Just trying out the website'),
    
    )

    GENDER_CHOICES = (
        ("male", "Male"),
        ("female", "Female"),
        ("other", "other"),
    )

    MOOD_CHOICES = (
        (5, "Over Joyed"),
        (4, "Happy"),
        (3, "Neutral"),
        (2, "Sad"),
        (1, "Depressed")
    )

    SLEEP_QUALITY_CHOICES = (
        (5, "Excellent"),
        (4, "Good"),
        (3, "Poor"),
        (2, "Fair"),
        (1, "Worse"),
    )

    MEDICATION_CHOICES = (
        (4, "Prescribed Medication"),
        (3, "Pharmacist"),
        (2, "I'm not taking any"),
        (1, "Prefer not to say"),
    )

    PHYSICAL_DISTRESS_CHOICES = (
        (2, "No"),
        (1, "Yes"),
    )

    PROFESSIONAL_HELP_CHOICES = (
        (2, "No"),
        (1, "Yes"),
    )

    STRESS_LEVEL_CHOICES = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    health_goal = models.CharField(max_length=250, choices=HEALTH_GOAL_CHOICES)
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField() 
    weight = models.PositiveIntegerField()
    mood = models.IntegerField(choices=MOOD_CHOICES)
    is_professional_help = models.IntegerField(choices=PROFESSIONAL_HELP_CHOICES)
    is_physical_distress = models.IntegerField(choices=PHYSICAL_DISTRESS_CHOICES)
    sleep_quality = models.IntegerField(choices=SLEEP_QUALITY_CHOICES)
    medications = models.IntegerField(choices=MEDICATION_CHOICES)
    other_mental_symptom = models.TextField()
    stress_level = models.PositiveIntegerField(choices=STRESS_LEVEL_CHOICES)

    def __str__(self):
        return f"{self.user.email} - {self.health_goal}"
    

    def calculate_mental_score(self):
        score_list = [int(self.mood), self.is_physical_distress, self.is_professional_help, self.sleep_quality, self.medications, self.stress_level]
        total_score = sum(score_list)
        max_score = len(self.MOOD_CHOICES) + len(self.PROFESSIONAL_HELP_CHOICES) + len(self.PHYSICAL_DISTRESS_CHOICES) + len(self.SLEEP_QUALITY_CHOICES) + len(self.MEDICATION_CHOICES) + len(self.STRESS_LEVEL_CHOICES)
        
        mental_score = (total_score / max_score) * 100
        return round(mental_score, 2)