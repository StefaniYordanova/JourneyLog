from django.db import models
from django.utils.text import slugify
from JourneyLog.mixins import CreationTimeStampMixin, NameMixin

# Create your models here.

class Destination(NameMixin, CreationTimeStampMixin):
    country = models.CharField(
        max_length=30,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    image_file = models.ImageField(
        upload_to='destination_images/',
        blank=True,
        null=True,
    )
    image_url = models.URLField(
        blank=True,
        null=True,
    )
    slug = models.SlugField(
        max_length=100,
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.name}, {self.country}"

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.country}")
        super().save(*args, **kwargs)
