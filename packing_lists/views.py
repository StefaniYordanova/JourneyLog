from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def add_item(request: HttpRequest) -> HttpResponse:
    return render(request, 'packing-item-add-page.html')

def delete_item(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'packing-item-delete-page.html')
