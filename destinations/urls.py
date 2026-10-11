from django.urls import path, include
from destinations import views

app_name = 'destinations'

urlpatterns = [
    path('add/', views.add_destination, name='add'),
    path('list/', views.list_destinations, name='list'),
    path('<slug:slug>/', include([
        path('', views.details_destination, name='details'),
        path('edit/', views.edit_destination, name='edit'),
        path('delete/', views.delete_destination, name='delete'),
    ])),
]