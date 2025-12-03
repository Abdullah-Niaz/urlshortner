from django.db import models
from django.utils import timezone
from .utils import generate_unique_slug


class URL(models.Model):
    original_url = models.URLField(max_length=2048)
    slug = models.CharField(max_length=16, unique=True, db_index=True)
    created_at = models.DateTimeField(default=timezone.now)
    clicks = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.slug} -> {self.original_url}"
