from  rest_framework import serializers
from project.models.project import *

class MediaSerializer(serializers.Serializer):
    class Meta:
        model = Media
        fields = '__all__'