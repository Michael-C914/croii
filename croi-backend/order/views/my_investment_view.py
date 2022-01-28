# DRF
from rest_framework import viewsets

# Models
from order.models.my_investment import MyInvestment

# Serializers
from order.serializer.my_investment_serializer import MyInvestmentSerializer


class MyInvestmentViewSet(viewsets.ModelViewSet):
    serializer_class = MyInvestmentSerializer
    queryset = MyInvestment.objects.all()