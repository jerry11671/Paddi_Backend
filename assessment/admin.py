from django.contrib import admin
from .models import HealthGoal, Assessment

admin.site.register(HealthGoal)
admin.site.register(Assessment)
