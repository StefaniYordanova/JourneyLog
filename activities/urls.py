from django.urls import path, include
from activities import views

app_name = 'activities'

urlpatterns = [
    path('add/', views.AddActivityView.as_view(), name='add'),
    path('list/', views.ListActivityView.as_view(), name='list'),
    path('<int:pk>/', include([
        path('edit/', views.EditActivityView.as_view(), name='edit'),
        path('delete/', views.delete_activity, name='delete'),
    ])),
]