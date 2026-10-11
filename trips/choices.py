from django.db import models

class TravelStyles(models.TextChoices):
    ADVENTURE = 'Adventure', 'Adventure'
    RELAXATION = 'Relaxation', 'Relaxation'
    SIGHTSEEING = 'Sightseeing', 'Sightseeing'

