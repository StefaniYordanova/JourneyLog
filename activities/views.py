from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .forms import ActivityCreateForm, ActivityEditForm, ActivityDeleteForm
from .models import Activity

# Class based view for creating activities:
class AddActivityView(CreateView):
    template_name = 'activities/activity-add-page.html'
    form_class = ActivityCreateForm

    def get_success_url(self):
        return reverse('trips:details', kwargs={'pk': self.object.trip.pk})

    # Function based view for creating activities:
# def add_activity(request: HttpRequest) -> HttpResponse:
#     form = ActivityCreateForm(request.POST or None)
#
#     if form.is_valid():
#         activity = form.save()
#         return redirect('trips:details', pk=activity.trip.pk)
#
#     context = {
#         "form": form,
#     }
#
#     return render(request, 'activities/activity-add-page.html', context)

# Class based view for editing activities:
class EditActivityView(UpdateView):
    model = Activity
    template_name = 'activities/activity-edit-page.html'
    form_class = ActivityEditForm

    def get_success_url(self):
        return reverse('trips:details', kwargs={'pk': self.object.trip.pk})

    # Function based view for editing activities:
# def edit_activity(request: HttpRequest, pk: int) -> HttpResponse:
#     activity = get_object_or_404(Activity, pk=pk)
#     trip_pk = activity.trip.pk
#     form = ActivityEditForm(request.POST or None, instance=activity)
#
#     if form.is_valid():
#         form.save()
#         return redirect('trips:details', pk=trip_pk)
#
#     context = {
#         "form": form,
#         "trip_pk": trip_pk,
#     }
#
#     return render(request, 'activities/activity-edit-page.html', context)

# Class based view for deleting activities:
class DeleteActivityView(DeleteView):
    model = Activity
    template_name = 'activities/activity-delete-page.html'
    form_class = ActivityDeleteForm

    def get_initial(self) -> dict:
        return self.object.__dict__

    def form_invalid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('trips:details', kwargs={'pk': self.object.trip.pk})

    # Function based view for deleting activities:
# def delete_activity(request: HttpRequest, pk: int) -> HttpResponse:
#     activity = get_object_or_404(Activity, pk=pk)
#     trip_pk = activity.trip.pk
#     form = ActivityDeleteForm(instance=activity)
#
#     if request.method == "POST":
#         activity.delete()
#         return redirect('trips:details', pk=trip_pk)
#
#     context = {
#         "form": form,
#         "trip_pk": trip_pk,
#     }
#
#     return render(request, 'activities/activity-delete-page.html', context)


# Class based view for displaying all activities:
class ListActivityView(ListView):
    model = Activity
    template_name = 'activities/activity-list-page.html'
    context_object_name = 'activities'
    paginate_by = 10

    def get_queryset(self):
        return Activity.objects.select_related('trip').order_by('-trip__start_date')

    # Function based view for displaying all activities:
# def list_activities(request: HttpRequest) -> HttpResponse:
#     activities = Activity.objects.select_related('trip').order_by('-trip__start_date')
#
#     context = {
#         "activities": activities,
#     }
#
#     return render(request, 'activities/activity-list-page.html', context)
