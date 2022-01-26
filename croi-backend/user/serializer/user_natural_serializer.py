# DRF
from rest_framework import serializers

# Models
from user.models import CustomUser, UserNatural
from user.serializer.custom_user_serializer import CustomUserSerializer


class UserNaturalSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = UserNatural
        fields = [
            'id',
            'user',
            'special_user',
            'DNI',
            'first_name',
            'last_name',
        ]
        read_only_fields = ['special_user']

    def create(self, validated_data):
        custom_user = validated_data.pop('user')
        user = CustomUser.objects.create(is_natural=True, **custom_user)
        user_natural = UserNatural.objects.create(user=user, **validated_data)
        return user_natural