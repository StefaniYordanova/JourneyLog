from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def add_trip(request: HttpRequest) -> HttpResponse:
    return render(request, 'trips/trip-add-page.html')

def edit_trip(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'trips/trip-edit-page.html')

def delete_trip(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'trips/trip-delete-page.html')

def details_trip(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'trips/trip-details-page.html')

def list_trip(request: HttpRequest) -> HttpResponse:
    return render(request, 'trips/trip-list-page.html')
