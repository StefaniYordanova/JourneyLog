from django.db.models import Q
from django.forms import modelform_factory
from django.shortcuts import reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from .forms import DestinationCreateForm, DestinationDeleteForm, SearchDestinationForm
from .models import Destination

class AddDestinationView(CreateView):
    template_name = 'destinations/destination-add-page.html'
    form_class = DestinationCreateForm
    success_url = reverse_lazy('destinations:list')


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
    success_url = reverse_lazy('destinations:list')
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
    paginate_by = 6

    def get_queryset(self):
        queryset = Destination.objects.order_by('-created_at')

        self.search_form = SearchDestinationForm(self.request.GET or None)

        if self.search_form.is_valid():
            query = self.search_form.cleaned_data.get('query')

            queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(country__icontains=query)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = self.search_form
        return context
