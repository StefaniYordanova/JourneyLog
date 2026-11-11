from django import forms
from destinations.models import Destination
from JourneyLog.mixins import DisabledFormFieldsMixin


class SearchDestinationForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'search-input-field',
            'placeholder': 'Search destinations...'
        })
    )


class BaseDestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        exclude = ['slug', 'user'] # excluding the user so that they won't be able to choose and add destinations to other users and see them
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

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit = True):
        destination = super().save(commit=False)

        if self.user is not None:
            destination.user = self.user
        if commit:
            destination.save()

        return destination


class DestinationCreateForm(BaseDestinationForm):
    ...

class DestinationDeleteForm(BaseDestinationForm, DisabledFormFieldsMixin):
    ...
