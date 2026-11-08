from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = 'accounts'

urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='accounts/login-page.html'), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('profile-details', views.ProfileDetailsView.as_view(), name='profile-details'),
]