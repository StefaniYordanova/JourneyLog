from django.urls import path, include
from destinations import views

app_name = 'destinations'

urlpatterns = [
    path('add/', views.add_destination, name='add'),
    path('<int:pk>/', include([
        path('', views.details_destination, name='details'),
        path('edit/', views.edit_destination, name='edit'),
        path('delete/', views.delete_destination, name='delete'),
    ])),
]