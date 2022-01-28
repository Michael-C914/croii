# DRF
from rest_framework import serializers

# Models
from order.models.my_bond import MyBond


class MyBondSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyBond
        fields = '__all__'
        #read_only_fields = ['my_action']