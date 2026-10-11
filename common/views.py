from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from trips.models import Trip

# Create your views here.

def home(request: HttpRequest) -> HttpResponse:
    upcoming_trip = Trip.objects.filter(
        is_completed=False,
    ).order_by('start_date').first()

    context = {
        'trip': upcoming_trip,
    }

    return render(request, 'common/home-page.html', context)
