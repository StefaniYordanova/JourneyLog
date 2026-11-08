from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import PhoneNumberValidator


class CustomUserModel(AbstractUser):
    phone_number = models.CharField(
        max_length=20,
        unique=True,
        validators=[
            PhoneNumberValidator(),
        ],
    )


class Profile(models.Model):
    user = models.OneToOneField(
        CustomUserModel,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='profile',
    )

    profile_picture = models.ImageField(
        upload_to='profile_pictures',
        null=True,
        blank=True,
        default='',
    )

    date_of_birth = models.DateField()

    bio = models.CharField(
        null=True,
        blank=True,
    )

    last_updated = models.DateField(
        auto_now=True,
    )