from django.db import models

from project.models.project import Project


class Investment(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="investment"
    )
    amount = models.IntegerField()
    interest_rate = models.FloatField()
