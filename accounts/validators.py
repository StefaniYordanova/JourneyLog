import re

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class PhoneNumberValidator:
    DEFAULT_ALLOWED_PREFIXES = ['+359', '+44', ]
    MESSAGE = "Enter a valid phone number"

    def __init__(self, allowed_prefixes: list[str] = DEFAULT_ALLOWED_PREFIXES, message: str = MESSAGE) -> None:
        self.allowed_prefixes = allowed_prefixes
        self.message = message

    def __call__(self, value: str) -> ValidationError | None:
        value = value.strip()

        if not any(value.startswith(prefix) for prefix in self.allowed_prefixes):
            raise ValidationError(self.message)

        if not re.match(r'^\+[0-9]+$', value):
            raise ValidationError(self.message)

