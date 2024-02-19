from django.db import models
from accounts.models import User

EMOTION_CHOICES = (
    ('Normal', 'normal'),
    ('Tired', 'tired'),
    ('Angry', 'angry'),
    ('Sad', 'sad'),
)

RATING_CHOICES = (
    ('positive', 'positive'),
    ('negative', 'negative'),
)

class Journal(models.Model):
    journal_user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    entry = models.TextField()
    stress_level = models.PositiveBigIntegerField(default=0)
    current_emotion = models.CharField(max_length=250, choices=EMOTION_CHOICES)
    whats_stressing_you = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    journal_rating = models.CharField(max_length=15, choices=RATING_CHOICES)

    def __str__(self):
        return self.title

