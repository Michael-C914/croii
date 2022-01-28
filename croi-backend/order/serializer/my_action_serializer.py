# DRF
from rest_framework import serializers

# Models
from order.models.my_action import MyAction


class MyActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyAction
        fields = '__all__'
        read_only_fields = ['my_action']