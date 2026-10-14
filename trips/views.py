from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TripCreateForm, TripEditForm, TripDeleteForm
from .models import Trip

# Create your views here.

def add_trip(request: HttpRequest) -> HttpResponse:
    form = TripCreateForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('trips:list')

    context = {
        "form": form,
    }

    return render(request, 'trips/trip-add-page.html', context)

def edit_trip(request: HttpRequest, pk: int) -> HttpResponse:
    trip = get_object_or_404(Trip, pk=pk)
    form = TripEditForm(request.POST or None, instance=trip)

    if form.is_valid():
        form.save()
        return redirect('trips:details', trip.pk)

    context = {
        "form": form,
        "trip": trip,
    }

    return render(request, 'trips/trip-edit-page.html', context)

def delete_trip(request: HttpRequest, pk: int) -> HttpResponse:
    trip = get_object_or_404(Trip, pk=pk)
    form = TripDeleteForm(instance=trip)

    if request.method == "POST":
        trip.delete()
        return redirect('trips:list')

    context = {
        "form": form,
        "trip": trip,
    }

    return render(request, 'trips/trip-delete-page.html', context)


def details_trip(request: HttpRequest, pk: int) -> HttpResponse:
    trip = get_object_or_404(
        Trip.objects.select_related('destination').prefetch_related(
            'activities', 'packing_items', 'travel_notes'
        ),
        pk=pk
    )

    context = {
        "trip": trip,
    }

    return render(request, 'trips/trip-details-page.html', context)

def list_trip(request: HttpRequest) -> HttpResponse:
    upcoming_trips = Trip.objects.select_related('destination').filter(
        is_completed=False,
    ).order_by('start_date')

    completed_trips = Trip.objects.select_related('destination').filter(
        is_completed=True,
    ).order_by('-end_date')

    context = {
        "upcoming_trips": upcoming_trips,
        "completed_trips": completed_trips,
    }

    return render(request, 'trips/trip-list-page.html', context)
