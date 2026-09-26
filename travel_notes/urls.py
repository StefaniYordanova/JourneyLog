from django.urls import path, include
from travel_notes import views

app_name = 'travel_notes'

urlpatterns = [
path('add/', views.add_note, name='add'),
    path('<int:pk>/', include([
        path('', views.details_note, name='details'),
        path('edit/', views.edit_note, name='edit'),
        path('delete/', views.delete_note, name='delete'),
    ])),
]