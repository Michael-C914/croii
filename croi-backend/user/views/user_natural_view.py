# DRF
from rest_framework import viewsets

# Models
from user.models import UserNatural

# Serializers
from user.serializer.user_natural_serializer import UserNaturalSerializer


class UserNaturalViewSet(viewsets.ModelViewSet):
    serializer_class = UserNaturalSerializer
    queryset = UserNatural.objects.all()