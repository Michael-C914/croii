# DRF
from rest_framework import viewsets

# Models
from user.models import SpecialUser

# Serializers
from user.serializer.special_user_serializer import SpecialUserSerializer


class SpecialUserViewSet(viewsets.ModelViewSet):
    serializer_class = SpecialUserSerializer
    queryset = SpecialUser.objects.all()