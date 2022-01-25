# DRF
from rest_framework import serializers

# Models
from user.models import UserNatural


class UserNaturalSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNatural
        fields = '__all__'
        read_only_fields = ['special_user']