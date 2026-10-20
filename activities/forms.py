from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from .models import Activity
from JourneyLog.mixins import DisabledFormFieldsMixin


class BaseActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = "__all__"
        widgets = {
            "date_and_time": forms.DateTimeInput(
                attrs={"type": "datetime-local", "class": "form-control"}
            )
        }

    def clean(self):
        cleaned_data = super().clean()
        date_and_time_activity = cleaned_data.get('date_and_time')
        trip = cleaned_data.get('trip')
        completed = cleaned_data.get('is_completed')

        if trip:
            if date_and_time_activity:
                activity_date = date_and_time_activity.date()

                if not (trip.start_date <= activity_date <= trip.end_date):
                    raise ValidationError({
                        "date_and_time": f"The activity date must be within the trip's duration "
                        f"({trip.start_date.strftime('%d.%m.%Y')} – {trip.end_date.strftime('%d.%m.%Y')}).",
                    })

            if completed and date.today() < trip.start_date:
                raise ValidationError({
                    "is_completed": "Activity cannot be completed before the trip has started!",
                })

        return cleaned_data

class ActivityCreateForm(BaseActivityForm):
    ...

class ActivityEditForm(BaseActivityForm):
    ...

class ActivityDeleteForm(DisabledFormFieldsMixin, BaseActivityForm):
    ...
