from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import CreateView, UpdateView, ListView
from .forms import ActivityCreateForm, ActivityEditForm, ActivityDeleteForm
from .models import Activity


class AddActivityView(LoginRequiredMixin, CreateView):
    template_name = 'activities/activity-add-page.html'
    form_class = ActivityCreateForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user

        return kwargs

    def get_success_url(self):
        return reverse('trips:details', kwargs={'pk': self.object.trip.pk})


class EditActivityView(UpdateView):
    model = Activity
    template_name = 'activities/activity-edit-page.html'
    form_class = ActivityEditForm

    def get_success_url(self):
        return reverse('trips:details', kwargs={'pk': self.object.trip.pk})


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


class ListActivityView(LoginRequiredMixin, ListView):
    model = Activity
    template_name = 'activities/activity-list-page.html'
    context_object_name = 'activities'

    def get_queryset(self):
        return Activity.objects.select_related('trip').filter(
            trip__destination__user=self.request.user,
        ).order_by('-trip__start_date')
