from django.db import models
from JourneyLog.mixins import NameMixin

# Create your models here.

class PackingItem(NameMixin):
    is_packed = models.BooleanField(
        default=False,
    )
    trips = models.ManyToManyField(
        to='trips.Trip',
        related_name='packing_items',
    )

    def __str__(self) -> str:
        return f"{self.name}"
