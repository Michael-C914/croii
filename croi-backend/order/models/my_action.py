from django.db import models

from order.models.order import Order
from project.models.action import Action

# Create your models here.


class MyAction(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="my_action"
    )
    action = models.ForeignKey(
        Action,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="my_action"
    )
    created_at = models.DateTimeField()
    voucher = models.ImageField(upload_to="image", null=True, blank=True)
    quantity = models.IntegerField()
    sale_price = models.FloatField()
    total_price = models.FloatField()
