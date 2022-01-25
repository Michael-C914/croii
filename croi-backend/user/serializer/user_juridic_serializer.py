# Django
# DRF
from rest_framework import serializers

# Models
from user.models import CustomUser, UserJuridic
from user.serializer.custom_user_serializer import CustomUserSerializer


class UserJuridicSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = UserJuridic
        fields = [
            'id',
            'user',
            'special_user',
            'RUC',
            'name',
            'manager',
        ]
        read_only_fields = ['special_user']

    def create(self, validated_data):
        custom_user = validated_data.pop('user')
        user = CustomUser.objects.create(is_juridic=True, **custom_user)
        user_juridic = UserJuridic.objects.create(user=user, **validated_data)
        return user_juridic
