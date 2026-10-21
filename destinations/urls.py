from django.urls import path, include
from destinations import views

app_name = 'destinations'

urlpatterns = [
    path('add/', views.AddDestinationView.as_view(), name='add'),
    path('list/', views.ListDestinationView.as_view(), name='list'),
    path('<slug:slug>/', include([
        path('', views.DetailDestinationView.as_view(), name='details'),
        path('edit/', views.EditDestinationView.as_view(), name='edit'),
        path('delete/', views.DeleteDestinationView.as_view(), name='delete'),
    ])),
]