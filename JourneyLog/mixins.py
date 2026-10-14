from django.db import models

# Mixins used for models:
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

# Mixins used for forms:
class DisabledFormFieldsMixin:
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for name in self.fields:
            self.fields[name].widget.attrs['disabled'] = 'disabled'