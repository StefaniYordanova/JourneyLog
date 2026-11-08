from django.contrib.auth import get_user_model, forms
from django.contrib.auth.forms import UserCreationForm
from django import forms

UserModel = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ("first_name", "last_name", "username",
                  "email", "phone_number", )
        widgets = {
            'first_name': forms.TextInput(attrs={
                'autofocus': 'autofocus',
            }),
        }
        