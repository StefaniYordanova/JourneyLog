from django.db import models
from JourneyLog.mixins import TitleMixin


# Create your models here.

class Activity(TitleMixin):
    date_and_time = models.DateTimeField()
    location = models.CharField(
        max_length=100,
    )
    trip = models.ForeignKey(
        to='trips.Trip',
        on_delete=models.CASCADE,
        related_name='activities',
    )
    is_completed = models.BooleanField(
        default=False,
    )

    def __str__(self) -> str:
        return f"{self.title}"
