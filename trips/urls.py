from django.urls import path, include
from trips import views

app_name = 'trips'

urlpatterns = [
    path('add/', views.AddTripView.as_view(), name='add'),
    path('list/', views.list_trip, name='list'),
    path('<int:pk>/', include([
        path('', views.details_trip, name='details'),
        path('edit/', views.EditTripView.as_view(), name='edit'),
        path('delete/', views.DeleteTripView.as_view(), name='delete'),
    ])),
]