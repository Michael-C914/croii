from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from project.serializers.serializersRequestForm import RequestFormSerializer
from rest_framework import viewsets
from project.models import *

class RequestFormViewSet(viewsets.ModelViewSet):
    serializer_class = RequestFormSerializer
    queryset = RequestForm.objects.all()
