from  rest_framework import serializers
from project.models.project import *

class RequestFormSerializer(serializers.Serializer):
    class Meta:
        model = RequestForm
        fields = '__all__'