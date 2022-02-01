from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from project.serializers.serializersRequestForm import RequestFormSerializer
from rest_framework import viewsets
from project.models import *

class RequestFormViewSet(viewsets.ModelViewSet):
    serializer_class = RequestFormSerializer
    queryset = RequestForm.objects.all()

class RequestFormViewSet2(APIView):
    def post(self, request, format=None):
        serializer = RequestFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    