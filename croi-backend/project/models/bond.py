from django.db import models

from project.models.project import Project


class Bond(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="bond"
    )
