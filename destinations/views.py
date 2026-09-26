from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def add_destination(request: HttpRequest) -> HttpResponse:
    return render(request, 'destinations/destination-add-page.html')

def edit_destination(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'destinations/destination-edit-page.html')

def delete_destination(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'destinations/destination-delete-page.html')

def details_destination(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'destinations/destination-details-page.html')
