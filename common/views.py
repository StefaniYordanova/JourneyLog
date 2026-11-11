from django.views.generic import TemplateView
from trips.models import Trip


class HomeView(TemplateView):
    template_name = 'common/home-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            upcoming_trip = Trip.objects.select_related('destination').filter(
                destination__user=self.request.user,
                is_completed=False,
            ).order_by('start_date').first()
        else:
            upcoming_trip = None

        context['trip'] = upcoming_trip
        return context
