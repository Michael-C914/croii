from  rest_framework import serializers
from project.models.project import *

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
    
    def create(self, validated_data):
        project = Project.objects.create(
            category = validated_data['category'],
            user_admin = validated_data['user_admin'],
            name = validated_data['name'],
            address = validated_data['address'],
            state = validated_data['state']
        )
        return project


    def update(self,  instance, validated_data):
        return super().update(instance, validated_data)
