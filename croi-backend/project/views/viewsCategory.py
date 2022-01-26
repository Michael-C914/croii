from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from project.serializers.serializersCategory import CategorySerializer
from rest_framework import viewsets
from project.models import *


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
