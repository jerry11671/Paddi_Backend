from .models import User, Profile
from rest_framework import serializers
from django.contrib.auth import get_user_model

from assessment.models import UserAssessmentData

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['phone_number', 'school', 'address', 'profile_pic']

    # def update(self, instance, validated_data):
    #     instance.phone_number = validated_data.get('phone_number')
    #     instance.school = validated_data.get('school')
    #     instance.address = validated_data.get('address')
    #     instance.profile_pic = validated_data.get('profile_pic')

    #     instance.save()
    #     return instance


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',  'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')

        if password != password2:
            raise serializers.ValidationError("Passwords do not match!!")
        
        return data

    def create(self, validated_data):
        validated_data.pop('password2', None)
        if get_user_model().objects.filter(email=self.validated_data['email']):
            raise serializers.ValidationError({'error': 'Email already exists!'})
        
        
        user = User.objects.create_user(
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            password = validated_data['password'],
        )
        user.is_active = True
        user.save()

        return user
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']



