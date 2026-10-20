from django import forms
from django.core.exceptions import ValidationError
from trips.models import Trip
from JourneyLog.mixins import DisabledFormFieldsMixin
from datetime import date

class BaseTripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = "__all__"
        error_messages = {
            "destination": {
                "invalid_choice": "Please select a valid destination.",
            },
            "number_of_travelers": {
                "min_value": "There must be at least one traveler.",
            },
        }
        widgets = {
            'start_date': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'Select start date'}
            ),
            'end_date': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'Select end date'}
            ),
        }

    def clean(self):
        cleaned_data = super().clean()
        completed = cleaned_data.get('is_completed')
        trip_end_date = cleaned_data.get('end_date')
        current_date = date.today()

        if completed and trip_end_date and current_date < trip_end_date:
            raise ValidationError({
                "is_completed": "Trip cannot be completed until it's finished!",
            })


class TripCreateForm(BaseTripForm):
    ...

class TripEditForm(BaseTripForm):
    ...

class TripDeleteForm(DisabledFormFieldsMixin, BaseTripForm):
    ...
