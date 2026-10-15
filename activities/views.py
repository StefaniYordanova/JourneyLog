from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ActivityCreateForm, ActivityEditForm, ActivityDeleteForm
from .models import Activity

# Create your views here.

def add_activity(request: HttpRequest) -> HttpResponse:
    form = ActivityCreateForm(request.POST or None)

    if form.is_valid():
        activity = form.save()
        return redirect('trips:details', pk=activity.trip.pk)

    context = {
        "form": form,
    }

    return render(request, 'activities/activity-add-page.html', context)

def edit_activity(request: HttpRequest, pk: int) -> HttpResponse:
    activity = get_object_or_404(Activity, pk=pk)
    trip_pk = activity.trip.pk
    form = ActivityEditForm(request.POST or None, instance=activity)

    if form.is_valid():
        form.save()
        return redirect('trips:details', pk=trip_pk)

    context = {
        "form": form,
        "trip_pk": trip_pk,
    }

    return render(request, 'activities/activity-edit-page.html', context)

def delete_activity(request: HttpRequest, pk: int) -> HttpResponse:
    activity = get_object_or_404(Activity, pk=pk)
    trip_pk = activity.trip.pk
    form = ActivityDeleteForm(instance=activity)

    if request.method == "POST":
        activity.delete()
        return redirect('trips:details', pk=trip_pk)

    context = {
        "form": form,
        "trip_pk": trip_pk,
    }

    return render(request, 'activities/activity-delete-page.html', context)

