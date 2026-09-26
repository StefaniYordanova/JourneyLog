from django.urls import path, include
from trips import views

app_name = 'trips'

urlpatterns = [
    path('add/', views.add_trip, name='add'),
    path('<int:pk>/', include([
        path('', views.delete_trip, name='details'),
        path('edit/', views.edit_trip, name='edit'),
        path('delete/', views.delete_trip, name='delete'),
    ])),
]