# DRF
from rest_framework import viewsets

# Models
from order.models.order import Order

# Serializers
from order.serializer.order_serializer import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()