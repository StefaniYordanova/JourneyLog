from django import forms
from destinations.models import Destination
from JourneyLog.mixins import DisabledFormFieldsMixin


class BaseDestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        exclude = ['slug', ]

class DestinationCreateForm(BaseDestinationForm):
    ...

class DestinationDeleteForm(BaseDestinationForm, DisabledFormFieldsMixin):
    ...
