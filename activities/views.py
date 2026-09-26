from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def add_activity(request: HttpRequest) -> HttpResponse:
    return render(request, 'activities/activity-add-page.html')

def delete_activity(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'activities/activity-delete-page.html')

