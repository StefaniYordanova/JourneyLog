from django import forms
from trips.models import Trip
from JourneyLog.mixins import DisabledFormFieldsMixin

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


class TripCreateForm(BaseTripForm):
    ...

class TripEditForm(BaseTripForm):
    ...

class TripDeleteForm(BaseTripForm, DisabledFormFieldsMixin):
    ...
