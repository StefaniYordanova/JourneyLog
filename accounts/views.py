from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from .forms import CustomUserCreationForm, CustomUpdateUserInfoForm

UserModel = get_user_model()


class RegistrationView(UserPassesTestMixin, CreateView):
    form_class = CustomUserCreationForm
    model = UserModel
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('common:home')

    def test_func(self) -> bool:
        return not self.request.user.is_authenticated


class UpdateUserInfoView(UpdateView):
    form_class = CustomUpdateUserInfoForm
    model = UserModel
    template_name = 'accounts/edit-profile-page.html'
    success_url = reverse_lazy('common:home')

    def get_object(self, queryset=None):
        return self.request.user


class CustomLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'accounts/logout-page.html'
    http_method_names = ['get', 'post', 'options']


class ProfileDetailsView(DetailView):
    model = UserModel
    template_name = 'accounts/profile-details-page.html'

    def get_object(self, queryset = None):
        return self.request.user
