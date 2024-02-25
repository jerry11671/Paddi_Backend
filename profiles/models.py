from django.db import models
from accounts.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='./profile_pic')
    phone_number = models.CharField(max_length=15)
    school = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.user
    
