from django.http import HttpRequest, HttpResponse
from django.shortcuts import reverse, get_object_or_404, render, redirect
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from .forms import TravelNoteCreateForm, TravelNoteEditForm, TravelNoteDeleteForm
from .models import TravelNote

class AddNoteView(CreateView):
    template_name = 'travel_notes/note-add-page.html'
    form_class = TravelNoteCreateForm

    def get_success_url(self):
        return reverse('trips:details', kwargs={'pk': self.object.trip.pk})


class EditNoteView(UpdateView):
    model = TravelNote
    template_name = 'travel_notes/note-edit-page.html'
    form_class = TravelNoteEditForm

    def get_success_url(self):
        return reverse('trips:details', kwargs={'pk': self.object.trip.pk})


class DetailNoteView(DetailView):
    model = TravelNote
    template_name = 'travel_notes/note-details-page.html'
    context_object_name = 'note'


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


class ListNoteView(ListView):
    model = TravelNote
    template_name = 'travel_notes/note-list-page.html'
    context_object_name = 'notes'

    def get_queryset(self):
        return TravelNote.objects.select_related('trip').order_by('-trip__start_date')
