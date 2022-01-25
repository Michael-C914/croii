# DRF
from rest_framework import serializers

# Models
from user.models import UserJuridic


class UserJuridicSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserJuridic
        fields = '__all__'
        read_only_fields = ['special_user']
