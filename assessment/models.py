from django.db import models
from accounts.models import User
from django.template.defaultfilters import slugify

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
    ("happy", "Happy"),
    ("sad", "Sad"),
    ("neutral", "Neutral"),
)

SLEEP_QUALITY_CHOICES = (
    ("excellent", "Excellent"),
    ("good", "Good"),
    ("poor", "Poor"),
    ("fair", "Fair"),
    ("worse", "Worse"),
)

MEDICATION_CHOICES = (
    ("prescribed medication", "Prescribed Medication"),
    ("pharmacist", "Pharmacist"),
    ("i'm not taking any", "I'm not taking any"),
    ("prefer not to say", "Prefer not to say"),
)

   

class HealthGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True)
    health_goal = models.CharField(choices=HEALTH_GOAL_CHOICES, max_length=250)

    def __str__(self):
        return self.health_goal
    

class Assessment(models.Model):
    health_goal = models.OneToOneField(HealthGoal, on_delete=models.CASCADE)
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    mood = models.CharField(max_length=100, choices=MOOD_CHOICES)
    is_professional_help = models.BooleanField()
    is_physical_distress = models.BooleanField()
    sleep_quality = models.CharField(max_length=100, choices=SLEEP_QUALITY_CHOICES)
    medications = models.CharField(max_length=100, choices=MEDICATION_CHOICES)
    other_mental_symptom = models.TextField()
    stress_level = models.PositiveIntegerField()

    def __str__(self):
        return self.health_goal.health_goal
    
