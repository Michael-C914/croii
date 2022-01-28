# DRF
from rest_framework import serializers

# Models
from order.models.my_investment import MyInvestment


class MyInvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyInvestment
        fields = '__all__'
        #read_only_fields = ['my_action']