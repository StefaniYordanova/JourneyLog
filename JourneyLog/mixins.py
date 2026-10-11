from django.db import models

class CreationTimeStampMixin(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateField(
        auto_now_add=True,
    )

class NameMixin(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(
        max_length=50,
    )

class TitleMixin(models.Model):
    class Meta:
        abstract = True

    title = models.CharField(
        max_length=50,
    )