from rest_framework import serializers

from .models import Journal

class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ['journal_user', 'title', 'entry', 'stress_level', 'current_emotion', 'whats_stressing_you', 'created_at', 'updated_at']

        
        def update(self, instance, **validated_data):
            instance.title = validated_data.get('title', instance.title)
            instance.entry = validated_data.get('entry', instance.entry)
            instance.stress_level = validated_data.get('stress_level', instance.stress_level)
            instance.current_emotion = validated_data.get('current_emotion', instance.current_emotion)
            instance.whats_stressing_you = validated_data.get('whats_stressing_you', instance.whats_stressing_you)

            instance.save()
            return instance

    


        
        