from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import TripCreateForm, TripEditForm, TripDeleteForm
from .models import Trip


class AddTripView(CreateView):
    template_name = 'trips/trip-add-page.html'
    form_class = TripCreateForm
    success_url = reverse_lazy('trips:list')


class EditTripView(UpdateView):
    model = Trip
    template_name = 'trips/trip-edit-page.html'
    form_class = TripEditForm

    def get_success_url(self):
        return reverse('trips:details', kwargs={'pk': self.object.pk})


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
