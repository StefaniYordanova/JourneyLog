from datetime import date
from django import forms
from django.core.exceptions import ValidationError
from django.db.models import Q
from JourneyLog.mixins import DisabledFormFieldsMixin
from trips.models import Trip


class SearchTripForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'search-input-field',
            'placeholder': 'Search trips...'
        })
    )


class BaseTripForm(forms.ModelForm):
    confirm_date_change = forms.BooleanField(
        required=False,
        label="I understand that changing these dates will permanently delete activities falling outside the new range."
    )

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
            'title': forms.TextInput(
                attrs={'placeholder': 'Enter title...'}
            ),
            'start_date': forms.DateInput(
                attrs={'type': 'date', }
            ),
            'end_date': forms.DateInput(
                attrs={'type': 'date', }
            ),
            'number_of_travelers': forms.NumberInput(
                attrs={'placeholder': 'Enter number of travelers...'}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.show_confirmation = False

    """
    This clean() method performs two key validations:
    1. The first one checks if the end_date of the trip is set to be before its start_date.
    2. The second one is focused on checking, when editing an already existing trip, whether any of the trip's already 
    created activities will fall outside the newly set duration range.
    """
    def clean(self):
        cleaned_data = super().clean()
        completed = cleaned_data.get('is_completed')
        trip_start_date = cleaned_data.get('start_date')
        trip_end_date = cleaned_data.get('end_date')
        confirm_checked = cleaned_data.get('confirm_date_change')
        current_date = date.today()

        if completed and trip_end_date and current_date < trip_end_date:
            raise ValidationError({
                "is_completed": "Trip cannot be completed until it's finished!",
            })

        if self.instance and self.instance.pk and trip_start_date and trip_end_date:
            invalid_activities = self.instance.activities.filter(
                Q(date_and_time__date__lt=trip_start_date) |
                Q(date_and_time__date__gt=trip_end_date)
            )

            if invalid_activities.exists():
                if not confirm_checked:
                    self.show_confirmation = True
                    raise ValidationError(
                        "⚠️ Warning: Changing this trip's dates will cause "
                        f"{invalid_activities.count()} existing activity/activities to fall outside "
                        "the new range. Please check the confirmation box below to proceed with deletion."
                    )

                self.out_of_bounds_activities = invalid_activities

        return cleaned_data


class TripCreateForm(BaseTripForm):
    pass


class TripEditForm(BaseTripForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TripDeleteForm(DisabledFormFieldsMixin, BaseTripForm):
    ...
