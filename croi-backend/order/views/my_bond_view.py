# DRF
#from rest_framework import viewsets
# from django.shortcuts import render
# from rest_framework import generics
from rest_framework import viewsets

# Models
from order.models.my_bond import MyBond

# Serializers
from order.serializer.my_bond_serializer import MyBondSerializer


class MyBondViewSet(viewsets.ModelViewSet):
    serializer_class = MyBondSerializer
    queryset = MyBond.objects.all()

    