from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def add_note(request: HttpRequest) -> HttpResponse:
    return render(request, 'note-add-page.html')

def edit_note(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'note-edit-page.html')

def details_note(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'note-details-page.html')

def delete_note(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'note-delete-page.html')
