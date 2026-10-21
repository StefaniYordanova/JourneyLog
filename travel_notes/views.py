from django.shortcuts import reverse
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
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


class DeleteNoteView(DeleteView):
    model = TravelNote
    template_name = 'travel_notes/note-delete-page.html'
    form_class = TravelNoteDeleteForm

    def get_initial(self) -> dict:
        return self.object.__dict__

    def form_invalid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('trips:details', kwargs={'pk': self.object.trip.pk})


class ListNoteView(ListView):
    model = TravelNote
    template_name = 'travel_notes/note-list-page.html'
    context_object_name = 'notes'

    def get_queryset(self):
        return TravelNote.objects.select_related('trip').order_by('-trip__start_date')
