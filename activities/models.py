from django.db import models

# Create your models here.

class Activity(models.Model):
    class Category(models.TextChoices):
        SIGHTSEEING ='SIGHTSEEING', 'Sightseeing & Attractions'
        FOOD = 'FOOD', 'Food & Dining'
        ADVENTURE ='ADVENTURE', 'Outdoor & Adventure'
        CULTURE ='CULTURE', 'Art, History & Culture'
        RELAXATION ='RELAXATION', 'Relaxation & Leisure'

