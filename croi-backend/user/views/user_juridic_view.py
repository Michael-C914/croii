# DRF
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

# Models
from user.models import UserJuridic

# Serializers
from user.serializer.user_juridic_serializer import UserJuridicSerializer


class UserJuridicViewSet(viewsets.ModelViewSet):
    serializer_class = UserJuridicSerializer
    queryset = UserJuridic.objects.all()
