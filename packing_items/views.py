from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PackingItemCreateForm
from trips.models import Trip
from .models import PackingItem

# Create your views here.

def add_item(request: HttpRequest, trip_pk) -> HttpResponse:
    form = PackingItemCreateForm(request.POST or None)
    trip = get_object_or_404(Trip, pk=trip_pk)
    existing_items = PackingItem.objects.all()

    if form.is_valid():
        item_name = form.cleaned_data.get('name').strip()

        packing_item = PackingItem.objects.filter(
            name__iexact=item_name,
        ).first()

        if not packing_item:
            packing_item = PackingItem.objects.create(
                name=item_name,
            )

        packing_item.trips.add(trip)
        return redirect('trips:details', pk=trip.pk)

    context = {
        "form": form,
        "trip": trip,
        "existing_items": existing_items,
    }

    return render(request, 'packing_lists/packing-item-add-page.html', context)

def remove_item(request: HttpRequest, trip_pk: int,item_pk: int) -> HttpResponse:
    trip = get_object_or_404(Trip, pk=trip_pk)
    packing_item = get_object_or_404(PackingItem, pk=item_pk)

    if request.method == "POST":
        trip.packing_items.remove(packing_item)
        return redirect('trips:details', pk=trip_pk)

    context = {
        "trip": trip,
        "item": packing_item,
    }

    return render(request, 'packing_lists/packing-item-remove-page.html', context)

def packing_lists(request: HttpRequest) -> HttpResponse:
    packing_items = PackingItem.objects.prefetch_related('trips').order_by('-trips__start_date')

    context = {
        'packing_items': packing_items,
    }

    return render(request, 'packing_lists/packing-lists-page.html', context)
