from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy

app_name = 'accounts'

urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='accounts/login-page.html'), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('profile-details', views.ProfileDetailsView.as_view(), name='profile-details'),

    # Change of password when we know it:
    path('password-change/', PasswordChangeView.as_view(
        template_name='accounts/password-change-page.html',
        success_url=reverse_lazy('accounts:password_change_done'),
    ), name='password_change'),
    path('password-change-done/', PasswordChangeDoneView.as_view(template_name='accounts/password-change-done-page.html'), name='password_change_done'),


    # Change of password when we have forgotten it:
    path(
        'password-reset/',
        PasswordResetView.as_view(
            template_name='accounts/password-reset-page.html',
            success_url=reverse_lazy('accounts:password_reset_done')
        ),
        name='password_reset'
    ),
    path(
        'password-reset/done/',
        PasswordResetDoneView.as_view(
            template_name='accounts/password-reset-done-page.html'
        ),
        name='password_reset_done'
    ),
    path(
        'password-reset/confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='accounts/password-reset-confirm-page.html',
            success_url=reverse_lazy('accounts:password_reset_complete')
        ),
        name='password_reset_confirm'
    ),
    path(
        'reset/done/',
        PasswordResetCompleteView.as_view(
            template_name='accounts/password-reset-complete-page.html'
        ),
        name='password_reset_complete'
    ),
]