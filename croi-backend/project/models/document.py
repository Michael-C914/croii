from django.db import models

from project.models.project import RequestForm


class DocumentProject(models.Model):
    request_id = models.ForeignKey(
        RequestForm,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="document_project"
    )
    image = models.ImageField(upload_to="documents", null=True)

    def __str__(self) -> str:
        return str(self.id)


class DocumentAction(models.Model):
    request_id = models.ForeignKey(
        RequestForm,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="document_action"
    )
    image = models.ImageField(upload_to="documents", null=True)

    def __str__(self) -> str:
        return str(self.id)


class DocumentInvestment(models.Model):
    request_id = models.ForeignKey(
        RequestForm,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="document_investment"
    )
    image = models.ImageField(upload_to="documents", null=True)

    def __str__(self) -> str:
        return str(self.id)


class DocumentBond(models.Model):
    request_id = models.ForeignKey(
        RequestForm,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="document_bond"
    )
    image = models.ImageField(upload_to="documents", null=True)

    def __str__(self) -> str:
        return str(self.id)
