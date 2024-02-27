from .models import User, Profile
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

from assessment.models import Assessment

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['phone_number', 'school', 'address', 'profile_pic']

    def update(self, instance, validated_data):
        instance.phone_number = validated_data.get('phone_number')
        instance.school = validated_data.get('school')
        instance.address = validated_data.get('address')
        instance.profile_pic = validated_data.get('profile_pic')

        instance.save()
        return instance


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=True)
    # profile = ProfileSerializer()
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

    def validate_password(self, value):
        # Use Django's password validation to ensure a strong password
        validate_password(value)
        return value

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
        Profile.objects.create(user=user)

        return user
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']



