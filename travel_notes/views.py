from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TravelNoteCreateForm, TravelNoteEditForm, TravelNoteDeleteForm
from .models import TravelNote

# Create your views here.

def add_note(request: HttpRequest) -> HttpResponse:
    form = TravelNoteCreateForm(request.POST or None)

    if form.is_valid():
        note = form.save()
        trip_pk = note.trip.pk
        return redirect('trips:details', pk=trip_pk)

    context = {
        "form": form,
    }

    return render(request, 'travel_notes/note-add-page.html', context)

def edit_note(request: HttpRequest, pk: int) -> HttpResponse:
    note = get_object_or_404(TravelNote, pk=pk)
    trip_pk = note.trip.pk
    form = TravelNoteEditForm(request.POST or None, instance=note)

    if form.is_valid():
        form.save()
        return redirect('trips:details', pk=trip_pk)

    context = {
        "form": form,
        "note": note,
    }

    return render(request, 'travel_notes/note-edit-page.html', context)

def details_note(request: HttpRequest, pk: int) -> HttpResponse:
    note = get_object_or_404(TravelNote, pk=pk)

    context = {
        "note": note,
    }

    return render(request, 'travel_notes/note-details-page.html', context)

def delete_note(request: HttpRequest, pk: int) -> HttpResponse:
    note = get_object_or_404(TravelNote, pk=pk)
    trip_pk = note.trip.pk
    form = TravelNoteDeleteForm(instance=note)

    if request.method == "POST":
        note.delete()
        return redirect('trips:details', pk=trip_pk)

    context = {
        "form": form,
    }

    return render(request, 'travel_notes/note-delete-page.html', context)
