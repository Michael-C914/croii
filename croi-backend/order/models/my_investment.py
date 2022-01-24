from django.db import models

from order.models.order import Order
from project.models.investment import Investment

# Create your models here.


class MyInvestment(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="my_investment"
    )
    action = models.ForeignKey(
        Investment,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="my_investment"
    )
    created_at = models.DateTimeField()
    voucher = models.ImageField(upload_to="image", null=True, blank=True)
    total_price = models.FloatField()
