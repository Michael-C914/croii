# DRF
from rest_framework import serializers

# Models
from user.models import SpecialUser


class SpecialUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialUser
        fields = '__all__'
        read_only_fields = ['special_user']