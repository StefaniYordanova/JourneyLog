from django.core.validators import MinLengthValidator
from django.db import models
from JourneyLog.mixins import CreationTimeStampMixin, TitleMixin

# Create your models here.

class TravelNote(CreationTimeStampMixin, TitleMixin):
    content = models.TextField(
        validators=[
            MinLengthValidator(10),
        ]
    )
    trip = models.ForeignKey(
        to='trips.Trip',
        on_delete=models.CASCADE,
        related_name='travel_notes',
    )

    def __str__(self) -> str:
        return f"{self.title}"
