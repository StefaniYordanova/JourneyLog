from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import Profile

UserModel = get_user_model()

class CustomUserCreationForm(UserCreationForm):

    date_of_birth = forms.DateField()

    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ("first_name", "last_name", "username",
                  "email", "phone_number", )
        widgets = {
            'first_name': forms.TextInput(attrs={
                'autofocus': 'autofocus',
            }),
        }

    def save(self, commit = True):
        user = super().save(commit=commit)

        profile = Profile(
            user=user,
            date_of_birth=self.cleaned_data['date_of_birth'],
        )

        if commit:
            profile.save()

        return user

class CustomUpdateUserInfoForm(UserChangeForm):
    password = None

    class Meta(UserChangeForm.Meta):
        model = UserModel
        fields = ("first_name", "last_name", "username",
                  "email", "phone_number")