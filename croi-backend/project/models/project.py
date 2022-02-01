from django.db import models
from ..choices import documents
from user.models import UserJuridic, UserNatural, CustomUser


# Create your models here.
class Category(models.Model):
    name_category = models.CharField(max_length=50)

    def __str__(self) -> str:
        return str(self.name_category)


class Project(models.Model):
    category = models.ForeignKey(
        Category,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="project"
    )
    user_admin = models.ForeignKey(
        CustomUser, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50)
    address = models.TextField()
    state = models.CharField(max_length=15)

    def __str__(self) -> str:
        return str(self.name)


class RequestForm(models.Model):
    '''user_juridic = models.ForeignKey(
        UserJuridic,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="request_form"
    )
    user_natural = models.ForeignKey(
        UserNatural,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="request_form"
    )
    proyect_integer = models.ForeignKey(
        Project,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="request_form"
    )'''
    description = models.TextField()
    type_documents = models.CharField(
        choices=documents, default='P', max_length=1)
    is_juridic = models.BooleanField()
    is_natural = models.BooleanField()
    email = models.CharField(max_length=15)
    phone = models.IntegerField()
    conditions = models.BooleanField()
    date = models.DateField()
    importance = models.CharField(max_length=15)

    def __str__(self) -> str:
        return str(self.id)


class Media(models.Model):
    project = models.ForeignKey(
        Project,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="media"
    )
    image = models.ImageField(upload_to="image", null=True)

    def __str__(self) -> str:
        return str(self.project.name)
