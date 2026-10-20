from django import forms
from destinations.models import Destination
from JourneyLog.mixins import DisabledFormFieldsMixin


class BaseDestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        exclude = ['slug', ]
        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "Enter name...",}
            ),
            "country": forms.TextInput(
                attrs={"placeholder": "Enter country...", }
            ),
            "description": forms.Textarea(
                attrs={"placeholder": "Add description (optional)...", }
            )
        }

class DestinationCreateForm(BaseDestinationForm):
    ...

class DestinationDeleteForm(BaseDestinationForm, DisabledFormFieldsMixin):
    ...
