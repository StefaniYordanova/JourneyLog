from django import forms
from .models import TravelNote
from JourneyLog.mixins import DisabledFormFieldsMixin


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

class TravelNoteCreateForm(BaseTravelNoteForm):
    ...

class TravelNoteEditForm(BaseTravelNoteForm):
    ...

class TravelNoteDeleteForm(DisabledFormFieldsMixin, BaseTravelNoteForm):
    ...