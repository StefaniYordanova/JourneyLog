from django.core.exceptions import ValidationError
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

    def clean(self):
        super().clean()

        if self.image_url and self.image_file:
            raise ValidationError({
                'image_file': "Please provide either the image url or the image file, NOT BOTH!",
                'image_url': "Please provide either the image url or the image file, NOT BOTH!"
            })

        if not self.image_url and not self.image_file:
            raise ValidationError({
                'image_file': "Please provide either an image url or an image file.",
                'image_url': "Please provide either an image url or an image file."
            })