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
