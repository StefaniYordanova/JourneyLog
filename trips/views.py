from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
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


class DeleteTripView(DeleteView):
    model = Trip
    template_name = 'trips/trip-delete-page.html'
    form_class = TripDeleteForm
    success_url = reverse_lazy('trips:list')

    def get_initial(self) -> dict:
        return self.object.__dict__

    def form_invalid(self, form):
        return super().form_valid(form)


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
