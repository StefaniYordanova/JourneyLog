from django.urls import path
from packing_items import views

app_name = 'packing_items'

urlpatterns = [
    path('add-item/<int:trip_pk>/', views.add_item, name='add'),
    path('remove-item/<int:trip_pk>/<int:item_pk>/', views.remove_item, name='remove'),
    path('list/', views.packing_lists, name='list'),
]