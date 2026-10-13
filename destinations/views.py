from django.forms import modelform_factory
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import DestinationCreateForm, DestinationDeleteForm
from .models import Destination

# Create your views here.

def add_destination(request: HttpRequest) -> HttpResponse:
    form = DestinationCreateForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('destinations:list')

    context = {
        'form': form,
    }

    return render(request, 'destinations/destination-add-page.html', context)

def edit_destination(request: HttpRequest, slug: slug) -> HttpResponse:
    destination = get_object_or_404(Destination, slug=slug)

    if request.user.is_staff:
        DestinationEditForm = modelform_factory(Destination, fields="__all__")
    else:
        DestinationEditForm = modelform_factory(Destination, exclude=["slug", ])

    form = DestinationEditForm(request.POST or None, request.FILES or None, instance=destination)

    if form.is_valid():
        form.save()
        return redirect('destinations:list')

    context = {
        "form": form,
    }

    return render(request, 'destinations/destination-edit-page.html', context)

def delete_destination(request: HttpRequest, slug: slug) -> HttpResponse:
    destination = get_object_or_404(Destination, slug=slug)
    form = DestinationDeleteForm(instance=destination)

    if request.method == "POST":
        destination.delete()
        return redirect('destinations:list')

    context = {
        "form": form,
    }

    return render(request, 'destinations/destination-delete-page.html', context)

def details_destination(request: HttpRequest, slug: slug) -> HttpResponse:
    destination = get_object_or_404(Destination, slug=slug)

    context = {
        "destination": destination,
    }

    return render(request, 'destinations/destination-details-page.html', context)

def list_destinations(request: HttpRequest) -> HttpResponse:
    all_destinations = Destination.objects.order_by('-created_at')

    context = {
        "destinations": all_destinations,
    }

    return render(request, 'destinations/destination-list-page.html', context)
