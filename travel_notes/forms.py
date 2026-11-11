from django import forms
from .models import TravelNote
from JourneyLog.mixins import DisabledFormFieldsMixin
from trips.models import Trip


class BaseTravelNoteForm(forms.ModelForm):
    class Meta:
        model = TravelNote
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={'placeholder': 'Enter title...'}
            ),
            'content': forms.Textarea(
                attrs={'placeholder': 'Add content...'}
            ),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user is not None:
            self.fields['trip'].queryset = Trip.objects.filter(
                destination__user=user,
            )


class TravelNoteCreateForm(BaseTravelNoteForm):
    ...

class TravelNoteEditForm(BaseTravelNoteForm):
    ...

class TravelNoteDeleteForm(DisabledFormFieldsMixin, BaseTravelNoteForm):
    ...