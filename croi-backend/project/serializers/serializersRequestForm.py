from  rest_framework import serializers
from project.models.project import *

class RequestFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestForm
        fields = '__all__'

    def create(self, validated_data):
        requestform = RequestForm.objects.create(
            #user_juridic = validated_data['user_juridic'],
            #user_natural = validated_data['user_natural'],
            #proyect_integer = validated_data['proyect_integer'],
            description = validated_data['description'],
            #type_documents = validated_data['type_documents'],
            is_juridic = validated_data['is_juridic'],
            is_natural = validated_data['is_natural'],
            email = validated_data['email'],
            phone = validated_data['phone'],
            conditions = validated_data['conditions'],
            date = validated_data['date'],
            importance = validated_data['importance'],
        )
        return requestform

    def update(self,  instance, validated_data):
        return super().update(instance, validated_data)