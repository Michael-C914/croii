from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.


class CustomUserManager(BaseUserManager):

    def create_superuser(self, email, password, username, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, password, username, **other_fields)

    def create_user(self, email, password, username, **other_fields):

        if not email:
            raise ValueError('You must provide an email address')

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            **other_fields
        )
        user.set_password(password)
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address', unique=True)
    username = models.CharField(max_length=110, null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_natural = models.BooleanField(default=False)
    is_juridic = models.BooleanField(default=False)
    is_project = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return str(self.email)


class SpecialUser(models.Model):
    state = models.CharField(max_length=50)
    bank_statement = models.CharField(max_length=50)


class UserJuridic(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='user_juridic'
    )
    special_user = models.OneToOneField(
        SpecialUser,
        on_delete=models.CASCADE,
        related_name='user_juridic'
    )
    RUC = models.CharField(max_length=11)
    name = models.CharField(max_length=50)
    manager = models.CharField(max_length=50)


class UserNatural(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='user_natural'
    )
    special_user = models.OneToOneField(
        SpecialUser,
        on_delete=models.CASCADE,
        related_name='user_natural'
    )
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    DNI = models.CharField(max_length=8)
    special_user = models.CharField(max_length=8)
