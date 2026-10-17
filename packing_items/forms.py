from django import forms


class PackingItemCreateForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Type or select an item ...',
            'class': 'form-control',
            'list': 'existing-items-list'  # This is used to connect the input field to the datalist
                                           # for autocomplete suggestions from existing items.
        })
    )