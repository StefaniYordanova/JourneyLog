from django.views.generic import TemplateView
from trips.models import Trip


class HomeView(TemplateView):
    template_name = 'common/home-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        upcoming_trip = Trip.objects.filter(
            is_completed=False,
        ).order_by('start_date').first()

        context['trip'] = upcoming_trip
        return context
