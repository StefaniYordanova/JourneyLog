from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def add_trip(request: HttpRequest) -> HttpResponse:
    return render(request, 'trip-add-page.html')

def edit_trip(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'trip-edit-page.html')

def delete_trip(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'trip-delete-page.html')

def details_trip(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'trip-details-page.html')

