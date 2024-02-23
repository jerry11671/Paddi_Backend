from . import models
from rest_framework import serializers

def min_max_validator(value):
    if value > 5:
        raise serializers.ValidationError("Value cannot be more than 5")
    elif value <=0:
        raise serializers.ValidationError("Value cannot be less than 0")
    else:
        return value
