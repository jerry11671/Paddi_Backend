from rest_framework import serializers

from .models import Journal

class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ['id', 'journal_user', 'journal_text', 'feeling', 'mood', 'rating', 'created_at', 'updated_at']


        def create(self, validated_data):
            journal = Journal.objects.create(journal_text=validated_data['journal_text'], feeling=validated_data['feeling'], mood=validated_data['mood'], rating=validated_data['rating'])
            return journal

        
        def update(self, instance, **validated_data):
            instance.journal_text = validated_data.get('title', instance.journal_text)
            instance.feeling = validated_data.get('entry', instance.feeling)
            instance.mood = validated_data.get('stress_level', instance.mood)
            
            instance.save()
            return instance

    


        
        