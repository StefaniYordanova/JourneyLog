from django.core.exceptions import ValidationError
from django.db import models
from JourneyLog.mixins import CreationTimeStampMixin, TitleMixin
from .choices import TravelStyles

# Create your models here.

class Trip(TitleMixin, CreationTimeStampMixin):
    destination = models.ForeignKey(
        to='destinations.Destination',
        on_delete=models.CASCADE,
        related_name='trips',
    )
    start_date = models.DateField()
    end_date = models.DateField()
    travel_style = models.CharField(
        max_length=20,
        choices=TravelStyles.choices,
        default=TravelStyles.SIGHTSEEING,
    )
    number_of_travelers = models.PositiveIntegerField()
    is_completed = models.BooleanField(
        default=False,
    )

    def __str__(self) -> str:
        return f"{self.title} - {self.travel_style}"

    def clean(self):
        super().clean()

        if self.start_date and self.end_date:
            if self.end_date <= self.start_date:
                raise ValidationError(
                    "End date must be after the start date!"
                )