from django.urls import path, include
from travel_notes import views

app_name = 'travel_notes'

urlpatterns = [
    path('add/', views.AddNoteView.as_view(), name='add'),
    path('list/', views.ListNoteView.as_view(), name='list'),
    path('<int:pk>/', include([
        path('', views.DetailNoteView.as_view(), name='details'),
        path('edit/', views.EditNoteView.as_view(), name='edit'),
        path('delete/', views.DeleteNoteView.as_view(), name='delete'),
    ])),
]