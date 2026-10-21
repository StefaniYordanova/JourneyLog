from django.forms import modelform_factory
from django.shortcuts import reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView

from .forms import DestinationCreateForm, DestinationDeleteForm
from .models import Destination

class AddDestinationView(CreateView):
    template_name = 'destinations/destination-add-page.html'
    form_class = DestinationCreateForm
    success_url = reverse_lazy('destinations:list')

    def post(self, request, *args, **kwargs):
        form = self.get_form_class()(request.POST, request.FILES)

        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)


class EditDestinationView(UpdateView):
    model = Destination
    template_name = 'destinations/destination-edit-page.html'

    def get_form_class(self):
        if self.request.user.is_staff:
            return modelform_factory(Destination, fields="__all__")
        return modelform_factory(Destination, exclude=["slug", ])

    def get_success_url(self):
        return reverse('destinations:details', kwargs={'slug': self.object.slug})


class DeleteDestinationView(DeleteView):
    model = Destination
    template_name = 'destinations/destination-delete-page.html'
    success_url = 'destinations:list'
    form_class = DestinationDeleteForm

    def get_initial(self) -> dict:
        return self.object.__dict__

    def form_invalid(self, form):
        return super().form_valid(form)


class DetailDestinationView(DetailView):
    model = Destination
    template_name = 'destinations/destination-details-page.html'
    context_object_name = 'destination'


class ListDestinationView(ListView):
    model = Destination
    template_name = 'destinations/destination-list-page.html'
    context_object_name = 'destinations'
    paginate_by = 10

    def get_queryset(self):
        return Destination.objects.order_by('-created_at')
