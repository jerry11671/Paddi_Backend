from django.db import models
from accounts.models import User

FEELING_CHOICES = (
    ('overjoyed', 'overjoyed'),
    ('happy', 'happy'),
    ('neutral', 'neutral'),
    ('sad', 'sad'),
    ('angry', 'angry')
)

class Journal(models.Model):
    journal_user = models.ForeignKey(User, on_delete=models.CASCADE)
    journal_text = models.TextField()
    feeling = models.CharField(max_length=250)
    mood = models.CharField(max_length=250)
    rating = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.journal_user)

