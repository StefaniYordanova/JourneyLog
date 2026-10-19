from django import template
from datetime import date

register = template.Library()


@register.filter()
def days_left(trip_start_date):
    """Calculates the days left to the upcoming trip"""
    result = trip_start_date - date.today()

    return result.days
