from django.db import models

from user.models import SpecialUser
from order.choices import states
# Create your models here.


class Order(models.Model):
    special_user = models.ForeignKey(
        SpecialUser,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="order"
    )
    total = models.FloatField()
    created_at = models.DateTimeField()
    state = models.CharField(choices=states, default='E', max_length=1)
