from django.urls import path
from packing_lists import views

app_name = 'packing_lists'

urlpatterns = [
    path('add-item/', views.add_item, name='add'),
    path('<int:pk>/delete/', views.delete_item, name='delete'),
]