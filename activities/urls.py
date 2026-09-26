from django.urls import path
from activities import views

app_name = 'activities'

urlpatterns = [
    path('add/', views.add_activity, name='add'),
    path('delete/<int:pk>', views.delete_activity, name='delete'),
]