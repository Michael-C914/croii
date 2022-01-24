from django.db import models

from project.models.project import Project


class Action(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="action"
    )
    stock = models.IntegerField()
    sale_price = models.FloatField()
    purchase_price = models.FloatField()
