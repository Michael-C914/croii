from  rest_framework import serializers
from project.models.project import *

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'
    
    def create(self, validated_data):
        media = Media.objects.create(
            project = validated_data['project'],
            image = validated_data['image'],
        )
        return media

    def update(self,  instance, validated_data):
        return super().update(instance, validated_data)