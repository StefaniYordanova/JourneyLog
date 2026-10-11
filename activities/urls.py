from django.urls import path, include
from activities import views

app_name = 'activities'

urlpatterns = [
    path('add/', views.add_activity, name='add'),
    path('<int:pk>/', include([
        path('edit/', views.edit_activity, name='edit'),
        path('delete/', views.delete_activity, name='delete'),
    ])),
]