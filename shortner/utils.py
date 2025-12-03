import string
import random
from django.apps import apps

DEFAULT_SLUG_LENGTH = 6
ALPHABET = string.ascii_letters + string.digits


def _random_slug(length=DEFAULT_SLUG_LENGTH):
    return ''.join(random.choices(ALPHABET, k=length))


def generate_unique_slug(length=DEFAULT_SLUG_LENGTH):
    """
    Generate a unique slug without directly importing the model.
    This avoids circular imports.
    """
    URL = apps.get_model('shortner', 'URL')  # dynamic model loader

    for _ in range(10000):
        slug = _random_slug(length)
        if not URL.objects.filter(slug=slug).exists():
            return slug

    raise RuntimeError(
        "Could not generate a unique slug. Increase slug length.")
